from icrawler.builtin import BingImageCrawler
from pathlib import Path

folder_path = Path('images')
folder_path.mkdir(parents=True, exist_ok=True)

dogs = [
    'トイ・プードル',
    'チワワ',
    'MIX犬',
    # '柴犬',
    # 'ミニチュア・ダックスフント',
    # 'ポメラニアン',
    # 'ミニチュア・シュナウザー',
    # 'フレンチ・ブルドッグ',
    # 'ヨークシャー・テリア',
    # 'シー・ズー',
    # 'マルチーズ',
    # 'カニーンヘン・ダックスフント',
    # 'ゴールデン・レトリーバー',
    # 'パグ',
    # 'ウェルシュ・コーギー・ペンブローク',
    # 'ラブラドール・レトリーバー',
    # 'パピヨン',
    # 'ジャック・ラッセル・テリア',
    # 'ミニチュア・ピンシャー',
    # 'ビション・フリーゼ'
    ]

for i, dog in enumerate(dogs):
    crawler = BingImageCrawler(storage={'root_dir': f'./images/{dog}'})

    max = 30
    filters = dict(license='commercial')
    crawler.crawl(keyword=dog, max_num=max, filters=filters)
