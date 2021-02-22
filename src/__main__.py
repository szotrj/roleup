import parliament

analyzed_policy = analyze_policy_string(policy_doc)
for f in analyzed_policy.findings:
  print(f)
