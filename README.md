# Discoxy users' manual

## About

Discoxyは、「Discord」をプロキシ環境下で動作するようにするためのPythonを用いたGUIアプリケーションです。

Windowsでは、Discoxyは単一のexe形式のアプリケーションとして提供されます。

そのため、**Pythonの<u>インストールや環境構築などは不要です。</u>**

Windows、MacOS、Linuxで動作します。



## How to Install

[こちらから最新の「discoxy-ver-*.zip」ファイルをダウンロードしてください。](https://discoxy.approvers.dev/releases)

ダウンロードしたファイルを解凍すると、`discoxy.exe`を起動できるようになります。

Discoxyは特別なライブラリなどを使用しないため、**どの場所に置かれていても正常に動作します。**



## How to Use



## Q&A

#### Q. Discordの場所を誤って編集したが、初期設定に戻したい。

**設定ファイルを削除して再度起動すると初期設定に戻ります。**

詳しくは、`高度な設定`の`設定ファイルの編集`をご覧ください。


#### Q. WindowsでDiscord起動ボタンを押すと、「応答なし」となる。

仕様上の問題で、Windowsで起動ボタンを押すと、一定時間が経過した後に、「応答なし」となります。



#### Q. 「入力された値に誤りがあります: Discordの場所」とエラーが表示される。

Discordの場所が誤っている可能性があります。

**Update.exeではなく、Discordの本体<u>Discord.exe</u>の場所を指定してください。**



#### Q. ようわからんし動かん。

`Contacts`よりご連絡ください。可能な限りサポートします。



#### Q. バグ報告や要望、フィードバックなどを送りたい。

大歓迎です。`Contacts`をご確認ください。お待ちしています。



## 高度な設定

#### 設定ファイルの編集

Discoxyでは、ユーザーが最後に起動した時に入力された設定を保存し、次回起動時に呼び出しています。

Windowsを利用している場合、設定ファイルには、以下のいずれかの方法でアクセスできます。

```%APPDATA%\approvers\discoxy\config_cache.ini```

```<ユーザーディレクトリ>\AppData\Roaming\approvers\discoxy\config_cache.ini```

Discoxyが設定ファイルを見つけられなかった場合、初期設定で設定ファイルを新規作成します。



## Contacts

[このプロジェクトのissueページ](https://discoxy.approvers.dev/issues)もしくは、製作者[こるく](https://twitter.com?Colk_)および[フライさん](https://twitter.com/loxygen_k)にお気軽にご連絡ください。

バグ報告やフィードバックなど、些細なことでもご連絡お待ちしています。



## Thanks

このソフトウェアは[こるく](https://twitter.com?Colk_)および[フライさん](https://twitter.com/loxygen_k)によって製作されました。

このソフトウェアは完全無料で使用することができますが、お菓子かなんかをくれると喜びます。

