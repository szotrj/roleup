import parliament


def parse_args():
    parser = argparse.ArgumentParser()
    #
    # ... configure command line arguments ...
    #
    return parser.parse_args()

def main():
    args = parse_args()
    analyze_policy(args)

def analyze_policy(policy_doc):
    analyzed_policy = parliament.analyze_policy_string(policy_doc)
    for f in analyzed_policy.findings:
        ef = parliament.enhance_finding(f)
        return vars(ef)

if __name__ == "__main__":
    main()
