#!/usr/bin/env python3
"""
产品页面多语言翻译脚本
将中文产品页面翻译成7种语言版本
"""

import re
import os
from pathlib import Path

# 产品列表
PRODUCTS = [
    'fiberglass-wax',        # 黄腊管
    'pvc-hose',              # PVC套管
    'pet-braided-sleeve',    # PET编织网管
    'fiberglass-inner-fiber', # 内纤外胶管
    'fiberglass-inner-rubber', # 内胶外纤管
]

# 语言列表
LANGUAGES = ['en', 'ko', 'vi', 'th', 'id', 'tr', 'ar']

# 产品名称翻译
PRODUCT_NAMES = {
    'fiberglass-wax': {
        'zh': '黄腊管',
        'en': 'Wax Tube',
        'ko': '왁스 튜브',
        'vi': 'Ống Sáp Vàng',
        'th': 'ท่อขี้ผึ้งเหลือง',
        'id': 'Tabung Lilin Kuning',
        'tr': 'Sarı Mum Tüpü',
        'ar': 'أنبوب شمع أصفر',
    },
    'pvc-hose': {
        'zh': 'PVC套管',
        'en': 'PVC Insulation Tube',
        'ko': 'PVC 튜브',
        'vi': 'Ống PVC',
        'th': 'ท่อ PVC',
        'id': 'Tabung PVC',
        'tr': 'PVC Tüp',
        'ar': 'أنبوب PVC',
    },
    'pet-braided-sleeve': {
        'zh': 'PET编织网管',
        'en': 'PET Braided Sleeve',
        'ko': 'PET 편조 슬리브',
        'vi': 'Lưới Đan PET',
        'th': 'ปลอกถัก PET',
        'id': 'Selubung Rajut PET',
        'tr': 'PET Örgü Manşon',
        'ar': 'كم شبكة PET',
    },
    'fiberglass-inner-fiber': {
        'zh': '内纤外胶玻璃纤维套管',
        'en': 'Inner Fiber Outer Adhesive Sleeve',
        'ko': '내섬유외접 슬리브',
        'vi': 'Ống Sợi Thủy Tinh Lớp Trong Lớp Ngoài',
        'th': 'ปลอกเส้นใยแก้วชั้นในชั้นนอก',
        'id': 'Selubung Fiberglass Lapisan',
        'tr': 'İç Fiber Dış Yapışkan Manşon',
        'ar': 'كم ألياف زجاج طبقي',
    },
    'fiberglass-inner-rubber': {
        'zh': '内胶外纤玻璃纤维套管',
        'en': 'Inner Adhesive Outer Fiber Sleeve',
        'ko': '내접외섬유 슬리브',
        'vi': 'Ống Sợi Thủy Tinh Lớp Trong Lớp Ngoài',
        'th': 'ปลอกเส้นใยแก้วชั้นในชั้นนอก',
        'id': 'Selubung Fiberglass Lapisan',
        'tr': 'İç Yapışkan Dış Fiber Manşon',
        'ar': 'كم ألياف زجاج طبقي',
    },
}

# 通用翻译字典
TRANSLATIONS = {
    'en': {
        '首页': 'Home',
        '关于我们': 'About Us',
        '玻璃纤维套管': 'Fiberglass Sleeve',
        '产品中心': 'Products',
        '联系我们': 'Contact',
        '查看详情': 'View Details',
        '技术参数': 'Technical Parameters',
        '耐压等级': 'Voltage Level',
        '连续使用温度': 'Operating Temperature',
        '材质': 'Material',
        '外观': 'Appearance',
        '特点': 'Features',
        '应用领域': 'Applications',
        '传统电机绕组绝缘': 'Traditional motor winding insulation',
        '变压器绝缘保护': 'Transformer insulation protection',
        '家用电器绝缘': 'Home appliance insulation',
        '经济型绝缘需求': 'Economical insulation needs',
        '产品细节展示': 'Product Details',
        '为什么选择': 'Why Choose',
        '经济实惠': 'Cost-effective',
        '传统工艺': 'Traditional Process',
        '性价比高': 'High Cost Performance',
    },
    'ko': {
        '首页': '홈',
        '关于我们': '회사 소개',
        '玻璃纤维套管': '유리섬유 슬리브',
        '产品中心': '제품',
        '联系我们': '연락처',
        '查看详情': '상세보기',
        '技术参数': '기술 매개변수',
        '耐压等级': '내압 등급',
        '连续使用温度': '사용 온도',
        '材质': '재질',
        '外观': '외관',
        '特点': '특징',
        '应用领域': '응용 분야',
        '传统电机绕组绝缘': '전통 모터 권선 절연',
        '变压器绝缘保护': '변압기 절연 보호',
        '家用电器绝缘': '가전 제품 절연',
        '经济型绝缘需求': '경제적 절연 솔루션',
        '产品细节展示': '제품 세부 정보',
        '为什么选择': '선택 이유',
        '经济实惠': '경제적',
        '传统工艺': '전통 공정',
        '性价比高': '높은 가성비',
    },
    'vi': {
        '首页': 'Trang Chủ',
        '关于我们': 'Giới Thiệu',
        '玻璃纤维套管': 'Ống Sợi Thủy Tinh',
        '产品中心': 'Sản Phẩm',
        '联系我们': 'Liên Hệ',
        '查看详情': 'Xem Chi Tiết',
        '技术参数': 'Thông Số Kỹ Thuật',
        '耐压等级': 'Cấp Độ Chịu Áp',
        '连续使用温度': 'Nhiệt Độ Sử Dụng',
        '材质': 'Chất Liệu',
        '外观': 'Ngoại Hình',
        '特点': 'Đặc Điểm',
        '应用领域': 'Ứng Dụng',
        '传统电机绕组绝缘': 'Cách Điện Cuộn Dây Động Cơ',
        '变压器绝缘保护': 'Bảo Vệ Cách Điện Biến Áp',
        '家用电器绝缘': 'Cách Điện Thiết Bị Gia Dụng',
        '经济型绝缘需求': 'Nhu Cầu Cách Điện Kinh Tế',
        '产品细节展示': 'Chi Tiết Sản Phẩm',
        '为什么选择': 'Tại Sao Chọn',
        '经济实惠': 'Kinh Tế',
        '传统工艺': 'Công Nghệ Truyền Thống',
        '性价比高': 'Hiệu Suất Cao',
    },
    'th': {
        '首页': 'หน้าแรก',
        '关于我们': 'เกี่ยวกับเรา',
        '玻璃纤维套管': 'ปลอกเส้นใยแก้ว',
        '产品中心': 'สินค้า',
        '联系我们': 'ติดต่อ',
        '查看详情': 'ดูรายละเอียด',
        '技术参数': 'พารามิเตอร์',
        '耐压等级': 'ระดับทนแรงดัน',
        '连续使用温度': 'อุณหภูมิใช้งาน',
        '材质': 'วัสดุ',
        '外观': 'ลักษณะ',
        '特点': 'คุณสมบัติ',
        '应用领域': 'การใช้งาน',
        '传统电机绕组绝缘': 'ฉนวนขดลวดมอเตอร์',
        '变压器绝缘保护': 'ป้องกันฉนวนหม้อแปลง',
        '家用电器绝缘': 'ฉนวนเครื่องใช้ไฟฟ้า',
        '经济型绝缘需求': 'ฉนวนราคาประหยัด',
        '产品细节展示': 'รายละเอียดสินค้า',
        '为什么选择': 'ทำไมต้องเลือก',
        '经济实惠': 'ประหยัด',
        '传统工艺': 'กระบวนการดั้งเดิม',
        '性价比高': 'คุ้มค่า',
    },
    'id': {
        '首页': 'Beranda',
        '关于我们': 'Tentang Kami',
        '玻璃纤维套管': 'Selubung Fiberglass',
        '产品中心': 'Produk',
        '联系我们': 'Hubungi',
        '查看详情': 'Lihat Detail',
        '技术参数': 'Parameter Teknis',
        '耐压等级': 'Tingkat Tegangan',
        '连续使用温度': 'Suhu Operasi',
        '材质': 'Material',
        '外观': 'Penampilan',
        '特点': 'Fitur',
        '应用领域': 'Aplikasi',
        '传统电机绕组绝缘': 'Isolasi Lilitan Motor',
        '变压器绝缘保护': 'Proteksi Isolasi Trafo',
        '家用电器绝缘': 'Isolasi Peralatan Rumah',
        '经济型绝缘需求': 'Kebutuhan Isolasi Ekonomis',
        '产品细节展示': 'Detail Produk',
        '为什么选择': 'Mengapa Memilih',
        '经济实惠': 'Ekonomis',
        '传统工艺': 'Proses Tradisional',
        '性价比高': 'Nilai Tinggi',
    },
    'tr': {
        '首页': 'Ana Sayfa',
        '关于我们': 'Hakkımızda',
        '玻璃纤维套管': 'Fiberglas Manşon',
        '产品中心': 'Ürünler',
        '联系我们': 'İletişim',
        '查看详情': 'Detayları Gör',
        '技术参数': 'Teknik Parametreler',
        '耐压等级': 'Gerilim Seviyesi',
        '连续使用温度': 'Çalışma Sıcaklığı',
        '材质': 'Malzeme',
        '外观': 'Görünüm',
        '特点': 'Özellikler',
        '应用领域': 'Uygulamalar',
        '传统电机绕组绝缘': 'Geleneksel Motor Sargı Yalıtımı',
        '变压器绝缘保护': 'Trafo Yalıtım Koruması',
        '家用电器绝缘': 'Ev Aletleri Yalıtımı',
        '经济型绝缘需求': 'Ekonomik Yalıtım İhtiyacı',
        '产品细节展示': 'Ürün Detayları',
        '为什么选择': 'Neden Seçmeli',
        '经济实惠': 'Ekonomik',
        '传统工艺': 'Geleneksel Süreç',
        '性价比高': 'Yüksek Değer',
    },
    'ar': {
        '首页': 'الرئيسية',
        '关于我们': 'عنا',
        '玻璃纤维套管': 'كم ألياف زجاج',
        '产品中心': 'المنتجات',
        '联系我们': 'اتصل بنا',
        '查看详情': 'عرض التفاصيل',
        '技术参数': 'المعايير الفنية',
        '耐压等级': 'مستوى الجهد',
        '连续使用温度': 'درجة حرارة التشغيل',
        '材质': 'المادة',
        '外观': 'المظهر',
        '特点': 'الميزات',
        '应用领域': 'التطبيقات',
        '传统电机绕组绝缘': 'عزل ملفات المحرك التقليدي',
        '变压器绝缘保护': 'حماية عزل المحول',
        '家用电器绝缘': 'عزل الأجهزة المنزلية',
        '经济型绝缘需求': 'احتياجات العزل الاقتصادية',
        '产品细节展示': 'تفاصيل المنتج',
        '为什么选择': 'لماذا تختار',
        '经济实惠': 'اقتصادي',
        '传统工艺': 'عملية تقليدية',
        '性价比高': 'قيمة عالية',
    },
}

def translate_product_page(product, lang):
    """翻译产品页面"""
    # 读取中文版本
    zh_file = f'products/{product}.html'
    if not os.path.exists(zh_file):
        print(f"  ⚠️  文件不存在: {zh_file}")
        return None
    
    with open(zh_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 应用翻译
    trans_dict = TRANSLATIONS.get(lang, {})
    translated = content
    
    # 翻译通用词汇
    for zh, foreign in trans_dict.items():
        translated = translated.replace(zh, foreign)
    
    # 翻译产品名称
    if product in PRODUCT_NAMES:
        product_name = PRODUCT_NAMES[product].get(lang, product)
        # 替换标题中的产品名称
        translated = re.sub(
            r'<title>[^<]+</title>',
            f'<title>{product_name} - YC INSULATION</title>',
            translated
        )
    
    # 更新语言属性
    if lang == 'ar':
        translated = translated.replace('<html lang="zh-CN">', '<html lang="ar" dir="rtl">')
    else:
        translated = translated.replace('<html lang="zh-CN">', f'<html lang="{lang}">')
    
    # 更新面包屑导航中的语言链接
    translated = translated.replace('../index.html', f'../index-{lang}.html')
    translated = translated.replace('href="../index.html"', f'href="../index-{lang}.html"')
    
    # 写入新文件
    output_file = f'products/{product}-{lang}.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    return output_file

def main():
    """主函数"""
    print("=" * 70)
    print("YC INSULATION 产品页面多语言翻译工具")
    print("=" * 70)
    print()
    
    total = len(PRODUCTS) * len(LANGUAGES)
    current = 0
    
    for product in PRODUCTS:
        print(f"\n正在翻译: {product}")
        print("-" * 70)
        
        for lang in LANGUAGES:
            current += 1
            output_file = translate_product_page(product, lang)
            if output_file:
                print(f"  [{current}/{total}] ✅ {lang.upper()}: {output_file}")
            else:
                print(f"  [{current}/{total}] ⚠️  {lang.upper()}: 跳过")
    
    print()
    print("=" * 70)
    print(f"翻译完成！共生成 {current} 个文件")
    print("=" * 70)

if __name__ == '__main__':
    main()