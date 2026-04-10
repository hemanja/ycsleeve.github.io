#!/usr/bin/env python3
"""
基于英语版本生成其他语言版本
使用替换翻译字典，保持HTML结构完整
"""

import re
from pathlib import Path

# 英语到各语言的翻译字典
EN_TO_LANG = {
    'vi': {
        # 基本词汇
        'Home': 'Trang Chủ',
        'About Us': 'Giới Thiệu',
        'Products': 'Sản Phẩm',
        'Factory': 'Nhà Máy',
        'Contact': 'Liên Hệ',
        'Professional Insulation Sleeve Manufacturer': 'Nhà Sản Xuất Ống Cách Điện Chuyên Nghiệp',
        'Specialized in insulation materials': 'Chuyên Vật Liệu Cách Điện',
        'Years of Experience': 'Năm Kinh Nghiệm',
        'Export Countries': 'Quốc Gia Xuất Khẩu',
        'Partner Customers': 'Khách Hàng Hợp Tác',
        'Browse Products': 'Xem Sản Phẩm',
        'Contact Us': 'Liên Hệ',
        
        # 产品名称
        'Fiberglass Silicone Sleeve': 'Ống Sợi Thủy Tinh Silicon',
        'Inner Fiber Outer Adhesive Sleeve': 'Ống Sợi Thủy Tinh Lớp Trong Lớp Ngoài',
        'Inner Adhesive Outer Fiber Sleeve': 'Ống Sợi Thủy Tinh Lớp Trong Lớp Ngoài',
        'PVC Coated Fiberglass Tube': 'Ống Sợi Thủy Tinh PVC',
        'Silicone Tube': 'Ống Silicon',
        'PVC Insulation Tube': 'Ống Cách Điện PVC',
        'Corrugated Tube': 'Ống Gợn Sóng',
        'PET Braided Expandable Sleeve': 'Lưới Đan PET Co Giãn',
        'Heat Shrink Tube': 'Ống Co Nhiệt',
        'Wax Tube': 'Ống Sáp Vàng',
        
        # 优势
        'Quality Assurance': 'Đảm Bảo Chất Lượng',
        'Independent Production': 'Sản Xuất Tự Chủ',
        'Fast Delivery': 'Giao Hàng Nhanh',
        'Global Export': 'Xuất Khẩu Toàn Cầu',
        'Professional Service': 'Dịch Vụ Chuyên Nghiệp',
        'Customization Service': 'Dịch Vụ Tùy Chỉnh',
        
        # 联系方式
        'Address': 'Địa Chỉ',
        'Phone': 'Điện Thoại',
        'Email': 'Email',
        'Inquiry': 'Yêu Cầu Báo Giá',
        'Name': 'Tên',
        'Company': 'Công Ty',
        'Message': 'Tin Nhắn',
        'Submit': 'Gửi',
        'Quick Links': 'Liên Kết Nhanh',
        'Main Products': 'Sản Phẩm Chính',
        'Contact Information': 'Thông Tin Liên Hệ',
        'All Rights Reserved': 'Bản Quyền',
        'View Details': 'Xem Chi Tiết',
        
        # 技术
        'Temperature Resistance': 'Khả Năng Chịu Nhiệt',
        'Voltage Resistance': 'Khả Năng Chịu Điện',
        'Certification': 'Chứng Nhận',
        'MOQ': 'Số Lượng Tối Thiểu',
        'Lead Time': 'Thời Gian Giao',
        'Free Sample': 'Mẫu Miễn Phí',
    },
    'th': {
        'Home': 'หน้าแรก',
        'About Us': 'เกี่ยวกับเรา',
        'Products': 'สินค้า',
        'Factory': 'โรงงาน',
        'Contact': 'ติดต่อ',
        'Professional Insulation Sleeve Manufacturer': 'ผู้ผลิตปลอกฉนวนมืออาชีพ',
        'Specialized in insulation materials': 'เชี่ยวชาญวัสดุฉนวน',
        'Years of Experience': 'ปีประสบการณ์',
        'Export Countries': 'ประเทศส่งออก',
        'Partner Customers': 'ลูกค้าคู่ค้า',
        'Browse Products': 'ดูสินค้า',
        'Contact Us': 'ติดต่อเรา',
        'Fiberglass Silicone Sleeve': 'ปลอกเส้นใยแก้วซิลิโคน',
        'Inner Fiber Outer Adhesive Sleeve': 'ปลอกเส้นใยแก้วชั้นในชั้นนอก',
        'Inner Adhesive Outer Fiber Sleeve': 'ปลอกเส้นใยแก้วชั้นในชั้นนอก',
        'PVC Coated Fiberglass Tube': 'ท่อเส้นใยแก้วเคลือบ PVC',
        'Silicone Tube': 'ท่อซิลิโคน',
        'PVC Insulation Tube': 'ท่อ PVC',
        'Corrugated Tube': 'ท่อลอน',
        'PET Braided Expandable Sleeve': 'ปลอกถัก PET',
        'Heat Shrink Tube': 'ท่อหดตัว',
        'Wax Tube': 'ท่อขี้ผึ้งเหลือง',
        'Quality Assurance': 'รับประกันคุณภาพ',
        'Independent Production': 'ผลิตเอง',
        'Fast Delivery': 'จัดส่งเร็ว',
        'Global Export': 'ส่งออกทั่วโลก',
        'Professional Service': 'บริการมืออาชีพ',
        'Customization Service': 'บริการตามสั่ง',
        'Address': 'ที่อยู่',
        'Phone': 'โทรศัพท์',
        'Email': 'อีเมล',
        'Inquiry': 'สอบถามราคา',
        'Name': 'ชื่อ',
        'Company': 'บริษัท',
        'Message': 'ข้อความ',
        'Submit': 'ส่ง',
        'Quick Links': 'ลิงก์ด่วน',
        'Main Products': 'สินค้าหลัก',
        'Contact Information': 'ข้อมูลติดต่อ',
        'All Rights Reserved': 'สงวนลิขสิทธิ์',
        'View Details': 'ดูรายละเอียด',
        'Temperature Resistance': 'ช่วงอุณหภูมิ',
        'Voltage Resistance': 'ระดับทนแรงดัน',
        'Certification': 'มาตรฐานรับรอง',
        'MOQ': 'ปริมาณขั้นต่ำ',
        'Lead Time': 'ระยะเวลาจัดส่ง',
        'Free Sample': 'ตัวอย่างฟรี',
    },
    'id': {
        'Home': 'Beranda',
        'About Us': 'Tentang Kami',
        'Products': 'Produk',
        'Factory': 'Pabrik',
        'Contact': 'Hubungi',
        'Professional Insulation Sleeve Manufacturer': 'Produsen Selubung Isolasi Profesional',
        'Specialized in insulation materials': 'Spesialis Material Isolasi',
        'Years of Experience': 'Tahun Pengalaman',
        'Export Countries': 'Negara Ekspor',
        'Partner Customers': 'Pelanggan Mitra',
        'Browse Products': 'Lihat Produk',
        'Contact Us': 'Hubungi Kami',
        'Fiberglass Silicone Sleeve': 'Selubung Fiberglass Silikon',
        'Inner Fiber Outer Adhesive Sleeve': 'Selubung Fiberglass Lapisan',
        'Inner Adhesive Outer Fiber Sleeve': 'Selubung Fiberglass Lapisan',
        'PVC Coated Fiberglass Tube': 'Tabung Fiberglass Lapisan PVC',
        'Silicone Tube': 'Tabung Silikon',
        'PVC Insulation Tube': 'Tabung PVC',
        'Corrugated Tube': 'Tabung Bergelombang',
        'PET Braided Expandable Sleeve': 'Selubung Rajut PET',
        'Heat Shrink Tube': 'Tabung Susut Panas',
        'Wax Tube': 'Tabung Lilin Kuning',
        'Quality Assurance': 'Jaminan Kualitas',
        'Independent Production': 'Produksi Mandiri',
        'Fast Delivery': 'Pengiriman Cepat',
        'Global Export': 'Ekspor Global',
        'Professional Service': 'Layanan Profesional',
        'Customization Service': 'Layanan Kustom',
        'Address': 'Alamat',
        'Phone': 'Telepon',
        'Email': 'Email',
        'Inquiry': 'Permintaan Penawaran',
        'Name': 'Nama',
        'Company': 'Perusahaan',
        'Message': 'Pesan',
        'Submit': 'Kirim',
        'Quick Links': 'Tautan Cepat',
        'Main Products': 'Produk Utama',
        'Contact Information': 'Informasi Kontak',
        'All Rights Reserved': 'Hak Cipta',
        'View Details': 'Lihat Detail',
        'Temperature Resistance': 'Rentang Suhu',
        'Voltage Resistance': 'Tingkat Tahan Tegangan',
        'Certification': 'Sertifikasi',
        'MOQ': 'Minimum Order',
        'Lead Time': 'Waktu Pengiriman',
        'Free Sample': 'Sampel Gratis',
    },
    'tr': {
        'Home': 'Ana Sayfa',
        'About Us': 'Hakkımızda',
        'Products': 'Ürünler',
        'Factory': 'Fabrika',
        'Contact': 'İletişim',
        'Professional Insulation Sleeve Manufacturer': 'Profesyonel Yalıtım Manşon Üreticisi',
        'Specialized in insulation materials': 'Yalıtım Malzemesi Uzmanı',
        'Years of Experience': 'Yıllık Deneyim',
        'Export Countries': 'İhracat Ülkesi',
        'Partner Customers': 'İş Ortağı',
        'Browse Products': 'Ürünleri Gör',
        'Contact Us': 'Bize Ulaşın',
        'Fiberglass Silicone Sleeve': 'Silikon Fiberglas Manşon',
        'Inner Fiber Outer Adhesive Sleeve': 'İç Fiber Dış Yapışkan Manşon',
        'Inner Adhesive Outer Fiber Sleeve': 'İç Yapışkan Dış Fiber Manşon',
        'PVC Coated Fiberglass Tube': 'PVC Kaplı Fiberglas Tüp',
        'Silicone Tube': 'Silikon Tüp',
        'PVC Insulation Tube': 'PVC Tüp',
        'Corrugated Tube': 'Oluklu Tüp',
        'PET Braided Expandable Sleeve': 'PET Örgü Manşon',
        'Heat Shrink Tube': 'Isı Daraltma Tüpü',
        'Wax Tube': 'Sarı Mum Tüpü',
        'Quality Assurance': 'Kalite Güvencesi',
        'Independent Production': 'Kendi Üretimi',
        'Fast Delivery': 'Hızlı Teslimat',
        'Global Export': 'Küresel İhracat',
        'Professional Service': 'Profesyonel Hizmet',
        'Customization Service': 'Özel Hizmet',
        'Address': 'Adres',
        'Phone': 'Telefon',
        'Email': 'E-posta',
        'Inquiry': 'Fiyat Sor',
        'Name': 'Adınız',
        'Company': 'Şirket Adı',
        'Message': 'Mesaj',
        'Submit': 'Gönder',
        'Quick Links': 'Hızlı Bağlantılar',
        'Main Products': 'Ana Ürünler',
        'Contact Information': 'İletişim Bilgileri',
        'All Rights Reserved': 'Tüm Hakları Saklıdır',
        'View Details': 'Detayları Gör',
        'Temperature Resistance': 'Sıcaklık Aralığı',
        'Voltage Resistance': 'Voltaj Seviyesi',
        'Certification': 'Sertifikasyon',
        'MOQ': 'Minimum Sipariş',
        'Lead Time': 'Teslimat Süresi',
        'Free Sample': 'Ücretsiz Numune',
    },
    'ar': {
        'Home': 'الرئيسية',
        'About Us': 'عنا',
        'Products': 'المنتجات',
        'Factory': 'المصنع',
        'Contact': 'اتصل بنا',
        'Professional Insulation Sleeve Manufacturer': 'مصنع أكمام عزل محترف',
        'Specialized in insulation materials': 'متخصص في مواد العزل',
        'Years of Experience': 'سنوات خبرة',
        'Export Countries': 'دول التصدير',
        'Partner Customers': 'عملاء شركاء',
        'Browse Products': 'تصفح المنتجات',
        'Contact Us': 'تواصل معنا',
        'Fiberglass Silicone Sleeve': 'كم ألياف زجاج سيليكون',
        'Inner Fiber Outer Adhesive Sleeve': 'كم ألياف زجاج طبقي',
        'Inner Adhesive Outer Fiber Sleeve': 'كم ألياف زجاج طبقي',
        'PVC Coated Fiberglass Tube': 'أنبوب ألياف زجاج مغلف PVC',
        'Silicone Tube': 'أنبوب سيليكون',
        'PVC Insulation Tube': 'أنبوب PVC',
        'Corrugated Tube': 'أنبوب مموج',
        'PET Braided Expandable Sleeve': 'كم شبكة PET',
        'Heat Shrink Tube': 'أنبوب انكماش حراري',
        'Wax Tube': 'أنبوب شمع أصفر',
        'Quality Assurance': 'ضمان الجودة',
        'Independent Production': 'إنتاج ذاتي',
        'Fast Delivery': 'توصيل سريع',
        'Global Export': 'تصدير عالمي',
        'Professional Service': 'خدمة محترفة',
        'Customization Service': 'خدمة مخصصة',
        'Address': 'العنوان',
        'Phone': 'الهاتف',
        'Email': 'البريد الإلكتروني',
        'Inquiry': 'طلب عرض سعر',
        'Name': 'الاسم',
        'Company': 'الشركة',
        'Message': 'الرسالة',
        'Submit': 'إرسال',
        'Quick Links': 'روابط سريعة',
        'Main Products': 'المنتجات الرئيسية',
        'Contact Information': 'معلومات الاتصال',
        'All Rights Reserved': 'جميع الحقوق محفوظة',
        'View Details': 'عرض التفاصيل',
        'Temperature Resistance': 'نطاق درجة الحرارة',
        'Voltage Resistance': 'مستوى الجهد',
        'Certification': 'الشهادة',
        'MOQ': 'الحد الأدنى للطلب',
        'Lead Time': 'فترة التسليم',
        'Free Sample': 'عينة مجانية',
    }
}

def translate_text(text, lang):
    """翻译文本"""
    result = text
    trans_dict = EN_TO_LANG.get(lang, {})
    
    # 按照短语长度排序，优先匹配长短语
    sorted_trans = sorted(trans_dict.items(), key=lambda x: len(x[0]), reverse=True)
    
    for en, foreign in sorted_trans:
        # 使用正则表达式进行大小写不敏感替换
        pattern = re.compile(re.escape(en), re.IGNORECASE)
        result = pattern.sub(foreign, result)
    
    return result

def translate_html_file(input_file, output_file, lang):
    """翻译HTML文件"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻译可见文本（在标签之间的文本）
    def translate_match(match):
        tag_content = match.group(1)
        # 如果是纯文本（不包含HTML标签），则翻译
        if not re.search(r'<[^>]+>', tag_content) and tag_content.strip():
            translated = translate_text(tag_content, lang)
            return f'>{translated}<'
        return match.group(0)
    
    # 处理标签间的内容
    translated = re.sub(r'>([^<]+)<', translate_match, content)
    
    # 更新语言属性
    if lang == 'ar':
        translated = translated.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
    else:
        translated = translated.replace('<html lang="en">', f'<html lang="{lang}">')
    
    # 更新canonical链接
    translated = translated.replace(
        'href="https://ycsleeve.com/index-en.html"',
        f'href="https://ycsleeve.com/index-{lang}.html"'
    )
    
    # 更新语言切换器
    lang_names = {
        'vi': 'Tiếng Việt',
        'th': 'ไทย',
        'id': 'Indonesia',
        'tr': 'Türkçe',
        'ar': 'العربية'
    }
    
    if lang in lang_names:
        # 移除英语的active
        translated = translated.replace('<a href="index-en.html" class="active">EN</a>', '<a href="index-en.html">EN</a>')
        # 添加当前语言的active
        translated = re.sub(
            f'<a href="index-{lang}\\.html">',
            f'<a href="index-{lang}.html" class="active">',
            translated
        )
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f'✅ 已生成: {output_file}')

def main():
    """主函数"""
    print("=" * 60)
    print("YC INSULATION 网站多语言翻译工具")
    print("基于英语版本生成其他语言版本")
    print("=" * 60)
    print()
    
    # 翻译主页
    print("正在翻译主页...")
    for lang in ['vi', 'th', 'id', 'tr', 'ar']:
        output_file = f'index-{lang}.html'
        print(f"  生成 {lang.upper()} 版本...", end=' ')
        translate_html_file('index-en.html', output_file, lang)
    
    print()
    print("=" * 60)
    print("翻译完成！")
    print("=" * 60)
    print()
    print("注意：")
    print("1. 请人工检查翻译结果，特别是专业术语")
    print("2. 技术参数（温度、电压等）保持不变")
    print("3. 阿拉伯语版本已添加RTL支持")
    print("4. SEO标题和描述需要进一步优化")

if __name__ == '__main__':
    main()