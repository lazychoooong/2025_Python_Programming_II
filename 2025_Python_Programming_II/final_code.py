# 구현 : 알고리즘 리셋 피드백 설문조사
# 구현 내용 -> 결과 저장: 날짜/시간 + 점수(원본/보정) + 총점/퍼센트 + (선택)주관식 피드백 저장
# 추가 : 부정문 질문(질문6)은 점수 방향을 뒤집어 계산에 반영 (보정점수 = 6 - 원본점수)

from datetime import datetime
# 추가 내용 1 : datetime
# 별도 txt 파일에 설문조사를 진행한 시간, 날짜 등을 저장할 수 있도록 사용한 모듈

def ask_rating(question):
    while True:
        ans = input(question + " ").strip()
        if ans.isdigit():
            n = int(ans)
            if 1 <= n <= 5:
                return n
        print("만족도 표시는 1부터 5 중에서 입력해주세요. 감사합니다.\n")


def ask_yn(prompt):
    while True:
        yn = input(prompt + " ").strip().upper()
        if yn in ("Y", "N"):
            return yn
        print("Y 또는 N으로 입력해주세요.\n")


def get_comment_by_range(percent):
    if percent < 20:
        return "만족도가 많이 낮게 나타났어요. 리셋 결과가 기대에 못 미쳤던 부분을 우선적으로 개선해볼게요."
    elif percent < 40:
        return "아직 아쉬운 점이 꽤 있는 것 같아요. 다양성/관련성 균형을 더 잘 맞추도록 조정해볼게요."
    elif percent < 60:
        return "보통 수준의 만족도예요. 현재 방식의 장점은 유지하면서 부족한 부분을 보완해볼게요."
    elif percent < 80:
        return "만족도가 꽤 높아요! 리셋이 다양한 관점 제공에 도움이 된 것으로 보이고, 디테일을 더 다듬어볼게요."
    else:
        return "만족도가 매우 높게 나왔어요! 지금 방향이 잘 맞는 것 같아요. 더 안정적으로 좋은 결과를 내도록 강화하겠습니다."


# 안내 문구 출력 -> 질문 제공, 만족도 리스트에 저장 -> 결과 제공 -> 주관식 피드백(선택) -> 피드백 txt 파일에 저장, 종료 의 단계로 진행
def main():
    print("안녕하세요! 알고리즘 리셋 시스템입니다.")
    print("간단한 피드백 설문조사를 통해 시스템을 더욱 좋은 방향으로 개선할 수 있도록 협조 부탁드립니다.\n")
    print("질문들을 읽어보시고 1-5까지 만족도 중 하나를 골라 입력해 주시면 결과에 반영되는 형식으로 진행됩니다. 그럼 설문조사를 시작합니다!")

    questions = [
        "질문 1. 리셋 이후 결과가 이전보다 더 도움이 되었나요? (1~5)",
        "질문 2. 리셋 이후 결과의 정확도/타당성이 이전보다 좋아졌나요? (1~5)",
        "질문 3. 결과의 출처가 다양했나요? (예: 공식/전문가/뉴스/커뮤니티 등) (1~5)",
        "질문 4. 결과가 중복 없이 새로운 정보를 제공했나요? (1~5)",
        "질문 5. 리셋 이후 결과의 원하는 답까지 도달하는 시간/클릭 수가 줄었나요? (1~5)",
        "질문 6. 다양성이 늘어난 대신 관련성이 떨어진 느낌이 있었나요? (1~5)",
        "질문 7. 결과를 신뢰할 수 있다고 느꼈나요? (1~5)",
        "질문 8. 리셋 버튼/옵션이 찾기 쉽다고 느끼셨나요? (1~5)",
        "질문 9. 리셋 버튼의 배치와 크기 등이 전체적으로 편리하다고 느끼셨나요? (1~5)",
        "질문 10. 전반적으로 리셋 기능을 다시 사용하고 싶나요? (1~5)",
    ]

    print()  # 한 줄 띄우기

    # 점수 입력 받기 (원본)
    raw_scores = []
    for q in questions:
        raw_scores.append(ask_rating(q))
        print()  # 질문 간 한 줄 띄우기

    # 점수 보정: 질문6은 부정문이므로 점수 뒤집기 (1<->5)
    adjusted_scores = raw_scores[:]
    adjusted_scores[5] = 6 - raw_scores[5]  # 질문6(인덱스 5) 보정

    # 점수 계산 (보정 점수 기준)
    total = sum(adjusted_scores)
    max_score = 50
    percent = (total / max_score) * 100

    # 결과 출력
    print("===== 설문 결과 =====")
    print(f"원본 점수: {raw_scores}")
    print(f"보정 점수: {adjusted_scores}  (질문6은 부정문이라 계산 시 6-입력값으로 보정됨)")
    print(f"총점(보정 기준): {total} / {max_score}")
    print(f"만족도: {percent:.1f}%")    # 추가 내용 2 : percent:.1f -> 만족도를 출력할 때 소수점 '첫째' 자리까지 출력하도록 설정
    comment = get_comment_by_range(percent)
    print(comment)
    print("=====================\n")

    yn = ask_yn("질문받은 내용 외에 별도로 하실 말씀이 있으신가요? 사용자님의 자세한 피드백은 더더욱 큰 도움이 됩니다. (Y/N) ")

    extra_feedback = ""
    if yn == "Y":
        extra_feedback = input("피드백 : ").strip()
        # 추가 내용 3 : strip -> 앞뒤 공백 제거에 사용함 (파프 12강, 파일과 예외처리에서 배운 것을 활용)

    filename = "user_feedback.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 추가 내용 1-2 : strftime() -> datetime 모듈에서 설문조사 실행한 시간을 문자열로 가져옴

    # 추가 내용 4 : 텍스트 파일 구현하기
    # 파일 열고 utf-8로 인코딩 / "a", 즉 이어쓰기 모드로 설정해서 설문조사 내역들이 삭제되지 않고 계속 추가되도록 구현
    with open(filename, "a", encoding="utf-8") as f:
        f.write("===== 설문 기록 =====\n")
        f.write(f"시간: {timestamp}\n")
        f.write(f"원본 점수: {raw_scores}\n")
        f.write(f"보정 점수: {adjusted_scores} (Q6 보정 적용)\n")
        f.write(f"총점(보정): {total}/{max_score}\n")
        f.write(f"만족도: {percent:.1f}%\n")
        f.write(f"멘트: {comment}\n")
        # 주관식 피드백이 있었을 경우 불러와서 같이 파일에 저장
        if yn == "Y":
            f.write(f"추가 피드백: {extra_feedback}\n")
        else:
            f.write("추가 피드백: (없음)\n")
        f.write("\n")

    if yn == "Y":
        print(f"\n소중한 피드백이 저장되었습니다. ({filename})")
        print("설문에 참여해 주셔서 정말 감사합니다! 프로그램을 종료합니다.")
    else:
        print(f"\n설문 결과가 저장되었습니다. ({filename})")
        print("설문에 참여해 주셔서 감사합니다! 프로그램을 종료합니다.")

main() 