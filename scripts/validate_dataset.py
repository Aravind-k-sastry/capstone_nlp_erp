import csv,json,pathlib,collections,sys
p=pathlib.Path(__file__).resolve().parents[1]/'data'/'p2p_conversations.csv'
required={'conversation_id','turn_id','conversation_context_json','user_prompt','expected_behavior','reference_tool_calls_json','expected_outcome_json','scenario_initial_state_json','validation_status'}
allowed={'create_purchase_order','submit_purchase_order','create_purchase_requisition','get_purchase_order','update_purchase_order','check_approval_authority','approve_purchase_order','get_supplier','create_goods_receipt','get_goods_receipt','get_goods_receipts','find_supplier_invoice','create_supplier_invoice','validate_invoice_match','get_purchase_order_status'}
with open(p,encoding='utf-8-sig',newline='') as fh:
 rows=list(csv.DictReader(fh))
assert required<=set(rows[0]);seen=set();groups=collections.Counter();fail=[]
for row in rows:
 try:
  assert row['turn_id'] not in seen;seen.add(row['turn_id']);groups[row['conversation_id']]+=1
  calls=json.loads(row['reference_tool_calls_json']);out=json.loads(row['expected_outcome_json']);state=json.loads(row['scenario_initial_state_json']);ctx=json.loads(row['conversation_context_json'])
  assert isinstance(calls,list) and isinstance(out,dict) and isinstance(state,dict) and isinstance(ctx,list)
  assert row['expected_behavior'] in ('execute','clarify','refuse')
  assert all(c['tool'] in allowed and isinstance(c['arguments'],dict) for c in calls)
  assert (row['expected_behavior']!='clarify') or not calls
  bindings=set()
  def refs(x):
   if isinstance(x,str) and x.startswith('$'):assert x[1:] in bindings,(row['turn_id'],x)
   if isinstance(x,dict):
    for v in x.values():refs(v)
   if isinstance(x,list):
    for v in x:refs(v)
  for c in calls:
   refs(c['arguments'])
   if 'result_binding' in c:bindings.add(c['result_binding'])
 except Exception as e:fail.append((row['turn_id'],str(e)))
assert not fail,fail[:10]
assert len(groups)==400 and len(rows)==420
print(f'PASS: {len(groups)} conversations, {len(rows)} user turns, {sum(groups.values())} rows, {len(allowed)} tool names, valid JSON and result bindings')
