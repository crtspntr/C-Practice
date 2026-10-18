import subprocess
import shutil
import sys

def run_tests(assignment_id: str) -> bool:
    print(f'1) Build project for {assignment_id}...')
    try:
        subprocess.run(['cmake', '-S', '.', '-B', 'build', '-G', 'MinGW Makefiles', '-DCMAKE_CXX_COMPILER=g++', '-DCMAKE_BUILD_TYPE=Debug'], check=True)
        subprocess.run(['cmake', '--build', 'build', '--parallel', '2'], check=True)
    except subprocess.CalledProcessError:
        return False

    print(f'2) Running tests for {assignment_id}...')
    cp = subprocess.run(['ctest', '--test-dir', 'build', '-R', assignment_id, '--output-on-failure'])
    return cp.returncode == 0

def post_grade(pr_number: str, passed: bool, note: str):
    status = 'PASS' if passed else 'FAIL'
    body = f'**Teacher grade (automated, partial)**\n- ctests: {status}\n- Notes: {note}'
    subprocess.run(['gh', 'pr', 'comment', pr_number, '--body', body], check=True)

def main():
    if len(sys.argv) < 3:
        print('Usage: python scripts/grade.py <assignment_id> <pr_number>')
        sys.exit(1)
    assignment_id, pr_number = sys.argv[1], sys.argv[2]
    passed = run_tests(assignment_id)
    post_grade(pr_number, passed, 'Automated check complete. Review logic and style.')

if __name__ == "__main__":
    main()
