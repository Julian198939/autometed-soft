from flask import Flask, request, render_template

app = Flask(__name__)

products = [
    {'category': '各類型商品、加車鈕、清單', 'name': '訂閱制商品 (iphone)', 'url': 'https://24h.pchome.com.tw/prod/DYAJJ0-1900GNUUG'},
    {'category': '各類型商品、加車鈕、清單', 'name': '競標商品 (正式站隱藏館)', 'url': 'https://24h.pchome.com.tw/prod/DGBJLX-A900G43WU'},
    {'category': '各類型商品、加車鈕、清單', 'name': 'O2O商品(輪胎)', 'url': 'https://24h.pchome.com.tw/prod/DXBN5C-A900GDEHZ'},
    {'category': '各類型商品、加車鈕、清單', 'name': 'DIY商品(組裝電腦)(有減額)', 'url': 'https://24h.pchome.com.tw/prod/DSAUW9-C900H533A'},
    {'category': '各類型商品、加車鈕、清單', 'name': '書店商品 (電子書)', 'url': 'https://24h.pchome.com.tw/books/prod/DJBQ33-D900CBAZF'},
    {'category': '各類型商品、加車鈕、清單', 'name': '18禁商品', 'url': 'https://24h.pchome.com.tw/prod/DECZ0O-A900GIRGN'},
    #------------------------------------------------------------------------------------------------------------------------------#
    {'category': '加車按鈕', 'name': '只有一顆[加入購物車]', 'url': 'https://24h.pchome.com.tw/prod/DEDB9C-A900EPOH9'},
    {'category': '加車按鈕', 'name': '加入購物車+立即購買', 'url': 'https://24h.pchome.com.tw/prod/DEABKQ-A900AEB4R'},
    {'category': '加車按鈕', 'name': '有貨通知我', 'url': 'https://24h.pchome.com.tw/prod/DEDJ06-A900DZU1B'},
    {'category': '加車按鈕', 'name': '已售完', 'url': 'https://24h.pchome.com.tw/prod/DCBA6K-A900AC4M4'},
    {'category': '加車按鈕', 'name': '尚未開賣(或搜尋「福利品」)', 'url': 'https://24h.pchome.com.tw/prod/DYAA78-A900H3HUQ'},
    {'category': '加車按鈕', 'name': '選購 (任選館單品頁)', 'url': 'https://24h.pchome.com.tw/prod/DAAT2G-B900FIA6G'},
    {'category': '加車按鈕', 'name': '訂閱制商品 (iphone)', 'url': 'https://24h.pchome.com.tw/prod/DYAJJ0-1900GNUUG'},
    {'category': '加車按鈕', 'name': '點我再折扣', 'url': 'https://24h.pchome.com.tw/prod/DPAE0C-A900C7QYE'},

    #------------------------------------------------------------------------------------------------------------------------------#
    
    {'category': '規格品、組合商品', 'name': '一般商品規格品(咖啡豆)', 'url': 'https://24h.pchome.com.tw/prod/DBATEI-A900ATQVV'},
    {'category': '規格品、組合商品', 'name': '一般商品規格品(滑鼠)', 'url': 'https://24h.pchome.com.tw/prod/DSAR1N-A900GMFU7'},
    {'category': '規格品、組合商品', 'name': '一般規格品(部分規格賣完)', 'url': 'https://24h.pchome.com.tw/prod/DQBX20-A900GE4RI'},
    {'category': '規格品、組合商品', 'name': '任選規格品', 'url': 'https://24h.pchome.com.tw/prod/DAAT3K-B900GM1ZS'},
    {'category': '規格品、組合商品', 'name': '組合商品規格品(水壺)', 'url': 'https://24h.pchome.com.tw/prod/DEBWJG-1900GMTUT'},
    {'category': '規格品、組合商品', 'name': '組合商品規格品(洗髮精)', 'url': 'https://24h.pchome.com.tw/prod/DAAAEA-1900GG2KP'},
    {'category': '規格品、組合商品', 'name': '組合商品規格品(洗衣)', 'url': 'https://24h.pchome.com.tw/prod/DAAK0O-1900GY1FD'},
    {'category': '規格品、組合商品', 'name': '組合商品規格品(任選5)', 'url': 'https://24h.pchome.com.tw/prod/DAAK0O-1900H3HFH'},
    {'category': '規格品、組合商品', 'name': '組合商品規格品(任選6)', 'url': 'https://24h.pchome.com.tw/prod/DAAA9B-1900GRS7D'},
    {'category': '規格品、組合商品', 'name': '組合商品規格品(任選10)', 'url': 'https://24h.pchome.com.tw/prod/DAABEB-1900GH5QG?fq=/S/DAABEB'},
    {'category': '規格品、組合商品', 'name': '組合商品非規格品(吹風機)(1)', 'url': 'https://24h.pchome.com.tw/prod/DMBF12-1900GQ3YF'},
    {'category': '規格品、組合商品', 'name': '組合商品非規格品(保健)(3)', 'url': 'https://24h.pchome.com.tw/prod/DBBW09-1900AYHAD'},
    {'category': '規格品、組合商品', 'name': '組合商品非規格品(保健)(6)', 'url': 'https://24h.pchome.com.tw/prod/DBDF00-1900C1N6F'},
    {'category': '規格品、組合商品', 'name': '組合商品非規格品(保養)(2)', 'url': 'https://24h.pchome.com.tw/prod/DDAD2P-1900GXJ65'},
    {'category': '規格品、組合商品', 'name': '組合商品非規格品(寵物)(15)', 'url': 'https://24h.pchome.com.tw/prod/DEBVHP-1900H7EHQ'},
    {'category': '規格品、組合商品', 'name': '組合商品 規格+非規格', 'url': 'https://24h.pchome.com.tw/prod/DQBE79-1900GTC9M'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選館 (滿額免運) (濕紙巾)', 'url': 'https://24h.pchome.com.tw/store/DAAT2G'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選品 (滿額免運)', 'url': 'https://24h.pchome.com.tw/prod/DAAT2G-B900FIA6G'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選館 (滿額出貨) (玩具)', 'url': 'https://24h.pchome.com.tw/store/DEAZJX'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選品 (滿額出貨)', 'url': 'https://24h.pchome.com.tw/prod/DEAZJX-B900B1Y2A'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選品 (獨立結帳) (生鮮)', 'url': 'https://24h.pchome.com.tw/prod/QFCH59-B900AQ7U7'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選品 (規格+價格上千)', 'url': 'https://24h.pchome.com.tw/prod/CCAA52-B49564075'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選區 (台隆手創館)', 'url': 'https://24h.pchome.com.tw/region/DEEO'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選區 (宜得利家居)', 'url': 'https://24h.pchome.com.tw/region/DQCI'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '任選區 (鄰家鮮生) - 已失效', 'url': 'https://24h.pchome.com.tw/region/DBDM'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '行銷活動館-商品 (星巴克膠囊)', 'url': 'https://24h.pchome.com.tw/prod/DBCO0Y-A900GGEGK'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '行銷活動館商品 (1件N元XXXX)', 'url': 'https://24h.pchome.com.tw/prod/DQBUAD-A900H2SGF'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '行銷活動館', 'url': 'https://24h.pchome.com.tw/store/?fq=/A/207745'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '有特賣變價', 'url': 'https://24h.pchome.com.tw/prod/DAAL4I-A9009F27R'},
    {'category': '任選館、特賣變價、行銷活動館', 'name': '特賣變價+任選館商品', 'url': 'https://24h.pchome.com.tw/prod/QFCLAQ-B900AP3T4'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '折價券', 'name': '有滿折券 (成人尿布、料理鍋)', 'url': 'https://24h.pchome.com.tw/prod/DMAGV2-A900BMAW0'},
    {'category': '折價券', 'name': '有單品券 (YSL、精品)', 'url': 'https://24h.pchome.com.tw/prod/DICKCI-A900GMBIP'},
    {'category': '折價券', 'name': '單品券+滿折券 (鍋具、精品)', 'url': 'https://24h.pchome.com.tw/prod/QCAM7N-A900A2S32'},
    {'category': '折價券', 'name': '有滿折券 (家電)', 'url': 'https://24h.pchome.com.tw/prod/DMAY0G-A900ARUAA'},
    {'category': '折價券', 'name': '無適用折價券', 'url': 'https://24h.pchome.com.tw/prod/DQCE27-A900GEO8K'},
    {'category': '折價券', 'name': '無折價券', 'url': 'https://24h.pchome.com.tw/prod/DXBK1O-A900FG0V4'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '贈品', 'name': '買就送1品 (洗衣機)', 'url': 'https://24h.pchome.com.tw/prod/DPAI1P-A900E4O8Q'},
    {'category': '贈品', 'name': '買就送多品 (洗衣機)', 'url': 'https://24h.pchome.com.tw/prod/DPAIH8-A900FSG00'},
    {'category': '贈品', 'name': '買就送多品 (隨身碟)', 'url': 'https://24h.pchome.com.tw/prod/DRAA0A-A900GXDLH'},
    {'category': '贈品', 'name': '買就送多品(精品錶)', 'url': 'https://24h.pchome.com.tw/prod/DIDW2C-A900H90GX'},
    {'category': '贈品', 'name': '買就送選規格', 'url': 'https://24h.pchome.com.tw/prod/DQCD3E-A900GJ2MV'},
    {'category': '贈品', 'name': '多選多贈品 (洗衣機)', 'url': 'https://24h.pchome.com.tw/prod/DPAI1P-A900GLVY1'},
    {'category': '贈品', 'name': '多選多選規格(機車)', 'url': 'https://24h.pchome.com.tw/prod/DXBK1O-A900FG0V4'},
    {'category': '贈品', 'name': '送完樣式 (隱藏館)', 'url': 'https://24h.pchome.com.tw/prod/QDAV0L-A9009UCU8'},

   #------------------------------------------------------------------------------------------------------------------------------#
    {'category': '送完樣式 (隱藏館)', 'name': '主(規)+贈(規) (機車)', 'url': 'https://24h.pchome.com.tw/prod/DXBK27-A900DSYTT'},
    {'category': '送完樣式 (隱藏館)', 'name': '主(規)+贈(規) (機車)', 'url': 'https://24h.pchome.com.tw/prod/DXBK0M-A900B0U1V'},
    {'category': '送完樣式 (隱藏館)', 'name': '主(規)+贈(規) (機車)', 'url': 'https://24h.pchome.com.tw/prod/DXBK3H-A900G5US7'},
    {'category': '送完樣式 (隱藏館)', 'name': '主(規)+贈', 'url': 'https://24h.pchome.com.tw/prod/DWAE3L-A900GI3DO'},
    {'category': '送完樣式 (隱藏館)', 'name': '贈品(規)', 'url': 'https://24h.pchome.com.tw/prod/DXBK27-A900DSYTT'},
    {'category': '送完樣式 (隱藏館)', 'name': '主(規)+贈(規)', 'url': 'https://24h.pchome.com.tw/prod/DMAAFN-A900GAHB8'},
    {'category': '送完樣式 (隱藏館)', 'name': '主(規)+贈(規)', 'url': 'https://24h.pchome.com.tw/prod/DQCD3E-A900GJ2MV'},
    {'category': '送完樣式 (隱藏館)', 'name': '組合(非規)+贈品+加購', 'url': 'https://24h.pchome.com.tw/prod/DPAF98-1900FZM28'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '出貨tag', 'name': '廠商出貨低溫-獨立結帳 (生鮮肉品)', 'url': 'https://24h.pchome.com.tw/prod/QFCH15-A900ACLVL'},
    {'category': '出貨tag', 'name': '廠商出貨低溫-非獨立結帳 (月餅)', 'url': 'https://24h.pchome.com.tw/prod/DBCZ0C-A900BNRSO'},
    {'category': '出貨tag', 'name': '獨立結帳 - 廠商出貨', 'url': 'https://24h.pchome.com.tw/prod/DXBK1O-A900FG0V4'},
    {'category': '出貨tag', 'name': '廠商出貨+預購+獨立結帳 (床架、家具)', 'url': 'https://24h.pchome.com.tw/prod/QFAA0E-A9006DR1R'},
    {'category': '出貨tag', 'name': '超大材積+PC非24h (冰箱)', 'url': 'https://24h.pchome.com.tw/prod/DPAC0X-A900BNDX2'},
    {'category': '出貨tag', 'name': '超大材積+PC非24h (沙發)', 'url': 'https://24h.pchome.com.tw/prod/DQAV26-A900GO4MU'},
    {'category': '出貨tag', 'name': '大材積+超大材積+PC非24h(冷氣)', 'url': 'https://24h.pchome.com.tw/prod/DPAF98-1900FZM28'},
    {'category': '出貨tag', 'name': '大材積+24h (衛生紙/箱)', 'url': 'https://24h.pchome.com.tw/prod/DAAG0S-A9005XWR4'},
    {'category': '出貨tag', 'name': '大材積+24h(微波爐、嬰兒床)', 'url': 'https://24h.pchome.com.tw/prod/DEAINZ-A900BL4VK'},
    {'category': '出貨tag', 'name': 'pchome出貨 (非24h)', 'url': 'https://24hstg9.pchome.com.tw/prod/DAAG8W-A900GP1PQ'},
    {'category': '出貨tag', 'name': 'pchome出貨 +低溫', 'url': 'https://24h.pchome.com.tw/prod/DBCP02-A900H87WZ'},
    {'category': '出貨tag', 'name': '電子票券', 'url': 'https://24h.pchome.com.tw/prod/DBCR07-A900GAJQC'},
    {'category': '出貨tag', 'name': '廠商預購商品(生鮮)', 'url': 'https://24h.pchome.com.tw/prod/DBCZ4R-A900GEG1P'},
    {'category': '出貨tag', 'name': '廠商預購商品(旅宿)', 'url': 'https://24h.pchome.com.tw/prod/DBCRPK-A900GP5F4'},
    {'category': '出貨tag', 'name': '廠商預購商品(家具電視櫃)', 'url': 'https://24h.pchome.com.tw/prod/DQCD0I-A900GF51W'},
    {'category': '出貨tag', 'name': '廠商預購商品(遊戲，PlayStation)', 'url': 'https://24h.pchome.com.tw/prod/DGBJCW-A900GS1OL'},
    {'category': '出貨tag', 'name': '寄倉預購(24h 預購)', 'url': 'https://24h.pchome.com.tw/prod/DHAEIC-A900FZCQB'},
    {'category': '出貨tag', 'name': '預購-陸續安排出貨', 'url': 'https://24h.pchome.com.tw/prod/DEDJ0V-A900FU2SQ'},
    {'category': '出貨tag', 'name': '任選滿額出貨 (app、大網都有) > 到區', 'url': 'https://24h.pchome.com.tw/prod/DBDM00-A900BROBI'},
    {'category': '出貨tag', 'name': '任選滿額免運 (app、大網都有) > 到區', 'url': 'https://24h.pchome.com.tw/prod/DEEO1E-A900GCMMJ'},
    {'category': '出貨tag', 'name': '任選滿額出貨 (app、大網都有) > 到館', 'url': 'https://24h.pchome.com.tw/prod/DEAZJX-B900B1Y2A'},
    {'category': '出貨tag', 'name': '任選滿額免運 (app有、大網沒有) > 到館', 'url': 'https://24h.pchome.com.tw/prod/DAAT3K-B900GM1ZS'},
    {'category': '出貨tag', 'name': '限購1品', 'url': 'https://24hstg9.pchome.com.tw/prod/DXBK27-A900DSYTT'},
    {'category': '出貨tag', 'name': '藥品仿單', 'url': 'https://24h.pchome.com.tw/prod/DABC9B-A900FBQAK'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': 'Fixed Bar', 'name': '一般商品_全部都有', 'url': 'https://24h.pchome.com.tw/prod/DDAD2P-1900GXJ65'},
    {'category': 'Fixed Bar', 'name': '一般商品_全部都有', 'url': 'https://24hstg9.pchome.com.tw/prod/DMAGOH-1900GT29G'},
    {'category': 'Fixed Bar', 'name': '任選商品_全部都有', 'url': 'https://24h.pchome.com.tw/prod/DAAT2G-B900FIA6G'},

     #------------------------------------------------------------------------------------------------------------------------------#
     
    {'category': '1040 AD', 'name': '1040 AD (AppleCare)', 'url': 'https://24h.pchome.com.tw/prod/DYAJG2-1900GSE8Z'},
    {'category': '1040 AD', 'name': '1040 AD (18禁)', 'url': 'https://24h.pchome.com.tw/prod/DECZ0O-A900GIRGN'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '書店範例', 'name': '商品詳情有5個標籤', 'url': 'https://24h.pchome.com.tw/books/prod/DJAP47-A900H85QF'},
    {'category': '書店範例', 'name': '商品詳情(圖+文)', 'url': 'https://24h.pchome.com.tw/books/prod/DJBP15-A900F7OLG'},
    {'category': '書店範例', 'name': '商品詳情(只有圖)', 'url': 'https://24hstg9.pchome.com.tw/books/prod/DJBF2H-A900H9VFS'},
    {'category': '書店範例', 'name': '商品詳情(只有文)', 'url': 'https://24h.pchome.com.tw/books/prod/DJAD3J-A900HBJII'},
    {'category': '書店範例', 'name': '有譯者', 'url': 'https://24h.pchome.com.tw/books/prod/DJAD3J-A900H9G5M'},
    {'category': '書店範例', 'name': '是KoBo電子書', 'url': 'https://24h.pchome.com.tw/books/prod/DJBQ2O-D900GBTD3'},
    {'category': '書店範例', 'name': '是電子書(讀墨)', 'url': 'https://24h.pchome.com.tw/books/prod/DJBN80-D900H5OVO'},
    {'category': '書店範例', 'name': '驗證作者連結', 'url': 'https://24h.pchome.com.tw/books/prod/DJAO21-A900H39JR'},
    {'category': '書店範例', 'name': '有行銷活動館', 'url': 'https://24h.pchome.com.tw/books/prod/DJAD3J-A900H9G5M'},
    {'category': '書店範例', 'name': '有1個以上優惠活動', 'url': 'https://24h.pchome.com.tw/books/prod/DJAH12-A900H856Y'},
    {'category': '書店範例', 'name': '舊主賣點', 'url': 'https://24h.pchome.com.tw/books/prod/DJBN80-D900H5OVO'},
    {'category': '書店範例', 'name': 'soft 404(6)', 'url': 'https://24h.pchome.com.tw/books/prod/DJBF2H-A900H9VFX'},

     #------------------------------------------------------------------------------------------------------------------------------#


    {'category': '主賣點', 'name': '主賣點看更多', 'url': 'https://24h.pchome.com.tw/prod/QFCH0E-A9009WY5L'},
    {'category': '主賣點', 'name': '主賣點html', 'url': 'https://24h.pchome.com.tw/prod/QFCH0E-A9009WY5L'},
    {'category': '主賣點', 'name': '舊主賣點 > 換行', 'url': 'https://24hstg9.pchome.com.tw/prod/QFCH3Y-B900A61PH'},
    {'category': '主賣點', 'name': '新主賣點 > 字多換行', 'url': 'https://24h.pchome.com.tw/prod/DEACGE-A900EOGUU'},
    {'category': '主賣點', 'name': '新主賣點 > 字多換行', 'url': 'https://24h.pchome.com.tw/prod/DCAHEK-A900GHA5X'},
    {'category': '主賣點', 'name': '新主賣點 > 有文字符號', 'url': 'https://24h.pchome.com.tw/prod/DBACWK-A900FMREV'},
    {'category': '主賣點', 'name': '新主賣點 > 新主賣點 > 字多換行', 'url': 'https://24h.pchome.com.tw/prod/DEAT0B-A900H0AZR'},
   
     #------------------------------------------------------------------------------------------------------------------------------#

      {'category': '銷售口號', 'name': '新主賣點 > 新主賣點 > 字多換行', 'url': 'https://24h.pchome.com.tw/prod/DBCO0N-A900ENDZT'},
      {'category': '銷售口號', 'name': '銷售口號寫作文', 'url': 'https://24h.pchome.com.tw/prod/DEAT0B-A900H0AZR'},
      {'category': '銷售口號', 'name': '銷售口號跑馬燈', 'url': 'https://24h.pchome.com.tw/prod/DMBJ0K-A900AW2WA'},
      {'category': '銷售口號', 'name': '銷售口號跑馬燈', 'url': 'https://24h.pchome.com.tw/prod/DECB0Y-A900BC1LQ'},
    
     #------------------------------------------------------------------------------------------------------------------------------#

      {'category': '相關商品', 'name': '有相關商品 (GIORDANO)', 'url': 'https://24h.pchome.com.tw/prod/DICU48-A900GR7B8'},
      {'category': '相關商品', 'name': '多個相關商品(床墊)', 'url': 'https://24h.pchome.com.tw/prod/DEABKY-A9009CGDJ'},
      {'category': '相關商品', 'name': '相關商品是任選品', 'url': 'https://24h.pchome.com.tw/prod/DEAKWZ-B900GYAVK'},
      {'category': '相關商品', 'name': '相關商品-賣完/關聯不全', 'url': 'https://24h.pchome.com.tw/prod/DMAGOH-1900GT29G'},
   
     #------------------------------------------------------------------------------------------------------------------------------#

      {'category': '推薦商品', 'name': '單品頁-別人也看 (PC)', 'url': 'https://24h.pchome.com.tw/prod/DMAGOH-1900GT29G'},
      {'category': '推薦商品', 'name': '單品頁-多種推薦-服飾商品', 'url': 'https://24h.pchome.com.tw/prod/DICU3A-A9009S5M1'},
      {'category': '推薦商品', 'name': '館頁-其他人也逛過', 'url': 'https://24h.pchome.com.tw/store/DEBW21'},
      {'category': '推薦商品', 'name': '單品頁-別人也看(洗髮精)', 'url': 'https://24h.pchome.com.tw/prod/DDAOE6-A900BKLQ3'},
   
     #------------------------------------------------------------------------------------------------------------------------------#

      {'category': '圖、燈箱', 'name': '有影片', 'url': 'https://24h.pchome.com.tw/prod/DQAUG6-A900GZ1XC'},
      {'category': '圖、燈箱', 'name': '無影片', 'url': 'https://24h.pchome.com.tw/prod/DDAOE6-A900BKLQ3'},
      {'category': '圖、燈箱', 'name': '影片+圖片', 'url': 'https://24h.pchome.com.tw/prod/DBAD3F-A45003336'},
      {'category': '圖、燈箱', 'name': '有規格大圖', 'url': 'https://24h.pchome.com.tw/prod/DSAR1N-A900GMFU7'},
      {'category': '圖、燈箱', 'name': '沒有規格大圖', 'url': 'https://24h.pchome.com.tw/prod/DQAU85-A900GK62P'},
   
     #------------------------------------------------------------------------------------------------------------------------------#
      
      {'category': '商品評價', 'name': '有商品評價', 'url': 'https://24h.pchome.com.tw/prod/DAAG8W-A900GP1PQ'},
      {'category': '商品評價', 'name': '一般規格品(有評價)', 'url': 'https://24hstg9.pchome.com.tw/prod/DSAR1N-A900GMFU7'},
      {'category': '商品評價', 'name': '組合商品規格品(有評價)', 'url': 'https://24hstg9.pchome.com.tw/prod/DAAAEA-1900GG2KP'},
      {'category': '商品評價', 'name': '評價文字寫很多', 'url': 'https://24hstg9.pchome.com.tw/prod/DECN08-A900BXZLI'},
      {'category': '商品評價', 'name': '有廠商回覆', 'url': 'https://24hstg9.pchome.com.tw/prod/DBAC89-A900FZRQL'},
      {'category': '商品評價', 'name': '評價文多+圖', 'url': 'https://24hstg9.pchome.com.tw/prod/DPAI1H-A900BRSG6'},
      {'category': '商品評價', 'name': '文多+多圖+廠商回覆', 'url': 'https://24hstg9.pchome.com.tw/prod/QFAB2F-A9008V8BG'},
      {'category': '商品評價', 'name': '驗證排序', 'url': 'https://24hstg9.pchome.com.tw/prod/DEEO1E-A900GCMMJ'},
      {'category': '商品評價', 'name': '評價文字超過須展開', 'url': 'https://24hstg9.pchome.com.tw/prod/DEAGSH-A900FHMN0'},
  
     #------------------------------------------------------------------------------------------------------------------------------#
     

    {'category': '優惠活動', 'name': '加碼金', 'url': 'https://24h.pchome.com.tw/prod/DECJ7H-A900H8XOK'},
    {'category': '優惠活動', 'name': 'p幣', 'url': 'https://24h.pchome.com.tw/prod/DSAEEH-A900GBKKM'},
    {'category': '優惠活動', 'name': '登記送', 'url': 'https://24h.pchome.com.tw/prod/DEDB6D-A900FQOB0'},
    {'category': '優惠活動', 'name': '登記抽', 'url': 'https://24h.pchome.com.tw/prod/DMAGZ8-1900HBTGG'},
    {'category': '優惠活動', 'name': '滿額贈', 'url': 'https://24h.pchome.com.tw/prod/DMAW1Z-A90094YNK'},
    {'category': '優惠活動', 'name': '現金積點', 'url': 'https://24h.pchome.com.tw/prod/DABC7Y-A900GQKE7'},
    {'category': '優惠活動', 'name': '現金積點', 'url': 'https://24h.pchome.com.tw/prod/DMBM2H-A900H5D5E'},
    {'category': '優惠活動', 'name': '現金積點', 'url': 'https://24h.pchome.com.tw/prod/QBAV09-A900APNDG'},
    {'category': '優惠活動', 'name': '優惠活動超過6個', 'url': 'https://24h.pchome.com.tw/prod/DWAE3L-A900GI3DO'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '價格', 'name': '只有網路價', 'url': 'https://24h.pchome.com.tw/prod/DBAY3D-A900AXLCI'},
    {'category': '價格', 'name': '網路價+建議售價', 'url': 'https://24h.pchome.com.tw/prod/DMBM2H-A900H5D5E'},
    {'category': '價格', 'name': '折扣價+網路價', 'url': 'https://24h.pchome.com.tw/prod/DQBUAD-A900H2SGF'},
    {'category': '價格', 'name': '訂閱', 'url': 'https://24h.pchome.com.tw/prod/DYAJIO-1900GNUOQ'},
    {'category': '價格', 'name': '驚喜優惠+折扣價', 'url': 'https://24h.pchome.com.tw/prod/DQBUAD-A900H2SGF'},
    {'category': '價格', 'name': '驚喜優惠+網路+建議', 'url': 'https://24h.pchome.com.tw/prod/DECBD3-A900BSXN4'},
    {'category': '價格', 'name': '顯示折扣後金額', 'url': 'https://24h.pchome.com.tw/prod/DEAA5J-A900GSTZN'},
    {'category': '價格', 'name': '驚喜優惠+折扣價+折價券', 'url': 'https://24h.pchome.com.tw/prod/DIBPX1-A900GGHDQ'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '404頁面', 'name': '商品頁面已經不存在(無)', 'url': 'https://24h.pchome.com.tw/prod/DMBI5Z-A900BZA2G'},
    {'category': '404頁面', 'name': '商品ID亂碼(無)', 'url': 'https://24h.pchome.com.tw/prod/DYALPF-A900GJ7EV'},
    {'category': '404頁面', 'name': '上架/不可單賣(有)', 'url': 'https://24h.pchome.com.tw/prod/DBDX08-A900GZA02'},
    {'category': '404頁面', 'name': '上架/不可單賣(Airtag)', 'url': 'https://24h.pchome.com.tw/prod/DYAJFM-A900BA39O'},
    {'category': '404頁面', 'name': '上架/不可單賣(有)', 'url': 'https://24h.pchome.com.tw/prod/DYAJFM-A900BA39O'},
    {'category': '404頁面', 'name': '贈品(無)', 'url': 'https://24h.pchome.com.tw/prod/DEAGSS-A900F4K0J'},
    {'category': '404頁面', 'name': '垃圾桶商品(有)', 'url': 'https://24h.pchome.com.tw/prod/DMBI5Z-A900BZA2G'},
    {'category': '404頁面', 'name': '下架商品(有)', 'url': 'https://24h.pchome.com.tw/prod/DSAUGY-C900G5M38'},

     #------------------------------------------------------------------------------------------------------------------------------#
     
    {'category': '好康加購', 'name': '好康加購(無規格)', 'url': 'https://24h.pchome.com.tw/prod/DBBB0W-19009JJQ2'},
    {'category': '好康加購', 'name': '好康加購(有規格)', 'url': 'https://24h.pchome.com.tw/prod/DEEO1E-A900GCMMJ'},
    {'category': '好康加購', 'name': '好康加購(18禁有規格)', 'url': 'https://24h.pchome.com.tw/prod/DECZ0O-A900GIRGN'},
    {'category': '好康加購', 'name': '好康加購(有規格+無規格)', 'url': 'https://24h.pchome.com.tw/prod/DEBWGJ-A90094HJW'},
    {'category': '好康加購', 'name': '主(規)+加(無規格)', 'url': 'https://24h.pchome.com.tw/prod/DYAI56-A900FPU04'},
    {'category': '好康加購', 'name': '主(規)+贈+加(規)', 'url': 'https://24h.pchome.com.tw/prod/DYAIAT-A900GO6R7'},
    {'category': '好康加購', 'name': '主(規)+贈+加(規/非規)', 'url': 'https://24h.pchome.com.tw/prod/DYAIAT-A900GQZC1'},
    {'category': '好康加購', 'name': '主(規)+贈+加(規/非規)', 'url': 'https://24h.pchome.com.tw/prod/DEDL03-A900FU7G8'},
    {'category': '好康加購', 'name': '主(規)+加(規)', 'url': 'https://24h.pchome.com.tw/prod/DABE2B-A900GHB20'},
    {'category': '好康加購', 'name': '主(規)+加(規)', 'url': 'https://24h.pchome.com.tw/prod/DXAB03-A900GFJTF'},
    {'category': '好康加購', 'name': '有貨通知我 > 加購不顯示', 'url': 'https://24h.pchome.com.tw/prod/DGADJH-A900G7MJL'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '滿N元送x點', 'name': '單筆消費+每筆訂單限贈一次', 'url': 'https://24h.pchome.com.tw/prod/DXBK1O-A900FG0V4'},
    {'category': '滿N元送x點', 'name': '單筆消費+活動期間限贈一次', 'url': 'https://24h.pchome.com.tw/prod/DXBK1O-A900FG0V4'},

     #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '滿N元,回饋X%, 回饋有上限Y點', 'name': '單筆消費+每筆訂單限贈一次', 'url': 'https://24h.pchome.com.tw/prod/DXBN1T-A900AV4JR'},
    {'category': '滿N元,回饋X%, 回饋有上限Y點', 'name': '單筆消費+活動期間限贈一次', 'url': 'https://24h.pchome.com.tw/prod/DEDB9C-A900EPOH9'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '刷聯名卡N%', 'name': '刷聯名卡N% (周四會出現)', 'url': 'https://24h.pchome.com.tw/prod/DCBV0W-A900H9A5Y'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': 'P幣效期', 'name': '30天', 'url': 'https://24h.pchome.com.tw/prod/DEDB9C-A900EPOH9'},
    {'category': 'P幣效期', 'name': '自訂(最多100天)', 'url': 'https://24h.pchome.com.tw/prod/DXBN1T-A900AV4JR'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '付款方式', 'name': '無限制-混付', 'url': 'https://24h.pchome.com.tw/prod/DECBD3-A900BSXN4'},
    {'category': '付款方式', 'name': '無限制-非混付', 'url': 'https://24h.pchome.com.tw/prod/DSAEEH-A900GBKKM'},
    {'category': '付款方式', 'name': '限信用卡-非混付', 'url': 'https://24h.pchome.com.tw/prod/DEDJ06-A900H0118'},
    {'category': '付款方式', 'name': '限支付-非混付', 'url': 'https://24h.pchome.com.tw/prod/DEDB1J-A900BBJQF'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '優惠活動-現金積點', 'name': '32. 單一帳號，活動期間只送一次，單筆訂單消費滿額', 'url': 'https://24h.pchome.com.tw/prod/DMBM2H-A900H5D5E'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '優惠活動-滿額贈', 'name': '購買金額=有限制', 'url': 'https://24h.pchome.com.tw/prod/DMAW1Z-A90094YNK'},

    #------------------------------------------------------------------------------------------------------------------------------#

    {'category': '優惠活動 - 加碼金(其他條件顯示文案)', 'name': '有限額N組', 'url': 'https://24h.pchome.com.tw/prod/DECJ7H-A900H8XOK'},

]



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword'].lower()
    searched_products = [product for product in products if keyword in product['name'].lower() or keyword in product['category'].lower()]
    return render_template('results.html', products=searched_products)

if __name__ == '__main__':
    app.run(debug=True, port=5005)

print("hi")