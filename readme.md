
# Markdown Converter App

このMarkdown Converter Appは、ChatGPT形式のMarkdown文書をTyporaやQiitaで使う形式に変換するStreamlitアプリケーションです。左側に元のMarkdownを入力し、変換ボタンを押すことで右側に変換後のMarkdownが表示されます。このアプリは特に、数式を含むMarkdown文書の変換に有効です。

## 特徴

- **シンプルなUI**: 誰でも簡単に使用できるクリーンなインターフェースを提供します。
- **即時プレビュー**: 変換後のMarkdownを即座にプレビューすることができます。
- **数式の変換**: LaTeX形式の数式をMathJax互換の形式に変換します。

## セットアップ方法

このアプリをローカルで実行するには、以下の手順に従ってください。

### 前提条件

- Python 3.6以上
- pip

### インストール方法

1. リポジトリをクローンするか、ソースコードをダウンロードします。
   ```
   git clone [リポジトリURL]
   cd [クローンしたディレクトリ]
   ```

2. 必要なPythonライブラリをインストールします。
   ```
   pip install -r requirements.txt
   ```

### 実行方法

Streamlitサーバーを起動します。
```
streamlit run app.py
```
ブラウザが自動的に開かない場合は、`http://localhost:8501`にアクセスしてください。

## 使い方

1. 左側のテキストボックスに変換したいMarkdown文書を貼り付けます。
2. 「Convert」ボタンを押します。
3. 右側に変換後のMarkdownが表示されます。Markdownとしてのプレビューも利用できます。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。詳細は`LICENSE`ファイルを参照してください。

