import os
import subprocess
from konlpy.tag import Okt

# 현재 Python 파일의 경로를 기준으로 JDK 경로 설정
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
JDK_PATH = os.path.join(PROJECT_DIR, 'jdk')  # 프로젝트 내 JDK 경로

# 1. 환경 변수 설정
os.environ['JAVA_HOME'] = JDK_PATH
os.environ['PATH'] = os.path.join(JDK_PATH, 'bin') + ':' + os.environ['PATH']

# 2. Java 실행 확인
try:
    subprocess.run(['java', '-version'], check=True)
    print("Java is correctly configured via Python.")
except Exception as e:
    print("Error with Java configuration:", e)
    exit(1)

# 3. Konlpy 테스트
try:
    okt = Okt()
    text = "자바와 파이썬은 함께 사용할 수 있습니다."
    print("형태소 분석 결과:", okt.morphs(text))
except Exception as e:
    print("Error with Konlpy:", e)
