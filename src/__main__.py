import parliament


def main():
    policy_doc = """{
        "Version": "2012-10-17",
        "Statement": {
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "*"
        }
    }"""

    analyze_policy(policy_doc)

def analyze_policy(policy_doc):
    analyzed_policy = parliament.analyze_policy_string(policy_doc)
    for f in analyzed_policy.findings:
        ef = parliament.enhance_finding(f)
        return vars(ef)

if __name__ == "__main__":
    main()
