import random


def play_game():
    # 1. コンピューターが1〜100の間でランダムな数字を選ぶ
    secret_number = random.randint(1, 100)
    attempts = 0

    print("--- 数当てゲームへようこそ！ ---")
    print("1から100までの数字を当ててみてね。")
    print("簡単は20回 普通は10回 難しいは5回の回数制限があります。")

    while True:  # 難易度選択
        level_input = input(
            "難易度を選択してください 簡単は1 普通は2 難しいは3を入力してください。"
        )
        if not level_input.isdigit():
            print("エラー：半角数字を入力してください。")
            continue
        level_input = int(level_input)
        if level_input == 1:
            life = 20
            print("簡単で開始します。")
            break
        elif level_input == 2:
            life = 10
            print("普通で開始します。")
            break
        elif level_input == 3:
            life = 5
            print("難しいで開始します。")
            break
        else:
            print(
                "レベルを選択してください 簡単は1 普通は2 難しいは3を入力してください。"
            )
            continue
    while True:
        # 2. ユーザーの入力を受け取る
        user_input = input("数字を入力してください: ")

        # 入力が数字かどうかチェック
        if not user_input.isdigit():
            print("エラー：半角数字を入力してください。")
            continue

        guess = int(user_input)
        attempts += 1  # 試行回数をカウント

        # 3. 判定ロジック
        if guess == secret_number:
            print(f"正解！おめでとう！ 🎉")
            print(f"あなたは {attempts} 回で当てました。")
            break  # 正解したのでループを抜ける
        elif abs(guess - secret_number) <= 5:
            print("めちゃくちゃ近いよ！")
        elif abs(guess - secret_number) <= 10:
            print("近いよ！")
        elif guess < secret_number:
            print("もっと大きいよ！ ↑")
        elif guess > secret_number:
            print("もっと小さいよ！ ↓")
        life -= 1  # ライフを減らす
        if life == 0:
            print(f"あなたはライフを使い切りました")
            break  # ライフを使い切ったのでループを抜ける


if __name__ == "__main__":
    play_game()
