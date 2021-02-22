import parliament


def analyze_policy(policy_doc):
    analyzed_policy = analyze_policy_string(policy_doc)
    for f in analyzed_policy.findings:
        ef = parliament.enhance_finding(f)
        return vars(ef)

if __name__ == "__main__":
    analyze_policy(policy)
