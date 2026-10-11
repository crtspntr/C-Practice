import subprocess
import shutil
import sys


def run_tests(pr_number: str) -> bool:
    print("1) Build project...")
    subprocess.run(["cmake", "-S", ".", "-B", "build", "-G", "MinGW Makefiles",
                    "-DCMAKE_CXX_COMPILER", "g++", "-DCMAKE_BUILD_TYPE=Debug"],
                   check=True)
    subprocess.run(["cmake", "--build", "build", "--parallel", "2"], check=True)

    print("2) Run tests...")
    cp = subprocess.run(["ctest", "--test-dir", "build", "--output-on-failure"])
    passed = cp.returncode == 0
    print("Result:", "PASS" if passed else "FAIL")
    return passed


def post_grade(pr_number: str, passed: bool, note: str):
    status = "PASS" if passed else "FAIL"
    body = f"**Teacher grade (automated, partial)**\n- ctests: {status}\n- Notes: {note}"
    cmd = ["gh", "pr", "comment", pr_number, "--body", body]
    subprocess.run(cmd, check=True)


def main():
    if not shutil.which("cmake") or not shutil.which("ctest") or not shutil.which("gh"):
        raise SystemExit("Missing required tools: cmake, ctest, gh, g++")

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/grade.py <assignment_id> <pr_number>")
    _, assignment_id, pr_number = sys.argv[:3]

    passed = run_tests(pr_number)
    note = ("Automated tool only: verify edge cases, explain reasoning, and "
            "code style before assigning points.")
    post_grade(pr_number, passed, note)


if __name__ == "__main__":
    main()
