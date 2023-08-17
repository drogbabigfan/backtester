'''
Backtest main file

1. 시가총액 조건
    - rank 활용하여 n% 이하, 이상 선택
    - KOSDAQ 기준 150위 이하, KOSPI 기준 200위 이하

2. 거래대금 조건
    - 일 거래대금 10억, 50억, 100억, 1000억 이상
    - n 평균 거래대금 10억, 50억, 100억, 1000억 이상

3. 거래량 조건
    - 일 거래량 10만주, 50만주, 100만주, 1000만주 이상
    - n 평균 거래량 10만주, 50만주, 100만주, 1000만주 이상

4. Turnover 조건
    - 일 turnover 1%, 5%, 10%, 20%, 50% 이상
    - n 평균 turnover 1%, 5%, 10%, 20%, 50% 이상

5. 가격 조건
    - 1000원 이하 종목 포함
    - 1000원 이하 종목 제외

6. 종목 수 조건
    - 10개, 20개, 30개, 40개, 50개, 100개

7. 모멘텀 조건
    - 1주, 2주, 1개월, 3개월, 6개월, 1년 -> 상대수익률
    - 절대수익률 > 0
    - 기하평균 수익률 or 산술평균 수익률

8. 리밸런싱 기간
    - 매일, 매주, 매월, 매분기

9. Momentum Filter 적용 방식
    - type1: Universe 적용 -> 잔존 종목 중 Momentum 계산 -> 상위 n개 선택, 하위 n개 선택
    - type2: Universe 적용 and Momentum 적용 -> 상위 n개 선택, 하위 n개 선택

10. 이평 Filter 적용 여부
    - 5선, 20선, 60선 기준 종가 up or down

11. Backetest 방식
    - DB에 Backtest 종류마다 list, result table 생성
    - Table명 기준: type에 따라 설정
    - backtest_list columns: 시가총액조건, 거래대금조건, 거래량조건, Turnover 조건, 가격조건, 종목수 조건, 모멘텀조건, 리밸런싱기간
    - backtest_result_columns: bt.run() 결과 사용

'''
