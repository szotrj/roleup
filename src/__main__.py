import parliament


def main(event):
    analyze_policy(event['policy'])

def analyze_policy(policy_doc):
    analyzed_policy = parliament.analyze_policy_string(policy_doc)
    for f in analyzed_policy.findings:
        ef = parliament.enhance_finding(f)
        return vars(ef)

if __name__ == "__main__":
    main(event)
