# 導入手順

対象: https://github.com/gaku213waka/gaku213waka

## 1. バックアップ

既存READMEを手元に保存してください。既存のSnakeや3D生成workflowがある場合は、この新しいworkflowと重複実行しないよう、そのファイルだけ削除・停止してください。

## 2. ファイルを配置

このフォルダのREADME.md、assets/、scripts/、.github/workflows/profile-visuals.ymlを、プロフィールリポジトリの直下へコピーしてコミットします。フォルダ「gaku213waka-profile」自体を一段下に置かないでください。

Windowsでは.githubが見えることを確認してください。GitHubの画面からアップロードする場合、.github/workflows/profile-visuals.ymlはAdd file → Create new fileで同じパスを入力して作成するのが確実です。

Gitを使う場合、既存のプロフィールリポジトリをcloneしたフォルダに上記ファイルをコピーし、以下を実行します。

```bash
git add README.md assets scripts .github/workflows/profile-visuals.yml
git commit -m "Refresh profile with pink contribution visuals"
git push
```

## 3. Actionsを初回実行

リポジトリのActions → Generate Profile Visuals → Run workflowを実行します。アップロード方法によってはpush時に自動実行されます。完了すると仮表示が実際のContributionのSnakeと3D画像に置き換わります。

workflowにcontents: writeを指定しており、通常は追加SecretやPATは不要です。組織等のポリシーで書き込みを禁止されている場合は、その制限の確認が必要です。保護されたブランチへの直接pushが禁止されている場合、このworkflowの最後のpushは失敗するため、生成画像をPRで更新する方式に変更してください。

毎日、日本時間03:25頃に更新します。GitHub側のスケジュールは遅延することがあります。

## 4. プロフィールを確認

https://github.com/gaku213waka を開きます。黒背景として見るにはGitHubのSettings → Appearanceでダークテーマを選んでください。READMEからページ全体の背景は指定できません。各SVG素材の黒背景はライトテーマでも維持されます。

## 同梱内容

- README.md: 完成版プロフィール
- assets/header.svg: 赤〜ピンクの波が動くヘッダー
- assets/footer.svg: フッター
- assets/ec.svg / behavior.svg / hotel.svg: 作品カード
- assets/generated/: 初回実行前の案内画像。実データはActionsで生成
- scripts/generate_3d.py: GitHub GraphQL APIから実際のContributionを取得して3D SVGを生成。Python標準ライブラリだけ使用
- .github/workflows/profile-visuals.yml: Snake＋3Dの日次生成

3D画像はこのパッケージ独自の実装です。参考テンプレのrainbow graphと完全同一ではありません。高さは件数の対数スケールです。実際のグラフに成長アニメーションは付けず、ヘッダー・Snake・ステータスの点に動きを付けています。

## 編集

配色は#0d1117（背景）、#ff006e（ピンク）、#ff1744（赤）、#ff4d9d（明るいピンク）。各SVG・READMEのURL・workflowのSnake色・Pythonのcolorsに記載されています。

ホテル分析は進行中として記載し、未確認のリポジトリリンクや成果値は入れていません。完成したらREADMEのCurrently Building部分に実際のリンクと成果を追記してください。

GitHub Stats、Streak、Activity Graph、Typing、Skill Icons、バッジは外部サービスです。障害・制限で一時的に表示されない場合があります。ローカル素材とActionsで生成した画像はこれらの表示サービスに依存しません。READMEの外部画像URLをブラウザで開くと表示状況を確認できます。

## 参考元

- デザインの参考: https://github.com/zyh3699/awesome-github-readme-profile
- Snake生成: https://github.com/Platane/snk
- Stats: https://github.com/anuraghazra/github-readme-stats
- Typing: https://github.com/DenverCoder1/readme-typing-svg
- Streak: https://github.com/DenverCoder1/github-readme-streak-stats
- Activity Graph: https://github.com/Ashutosh00710/github-readme-activity-graph
- Skill Icons: https://github.com/tandpfun/skill-icons

上記の参考テンプレのコードや画像をコピーせず、独自の素材とREADMEを作成しています。
