#!/usr/bin/env python3
"""
批量翻译脚本 - YC INSULATION网站多语言版本生成
将中文页面翻译成：vi(越南语)、th(泰语)、id(印尼语)、tr(土耳其语)、ar(阿拉伯语)
"""

import os
import re
from pathlib import Path

# 翻译字典 - 常用词汇和短语
TRANSLATIONS = {
    'vi': {  # 越南语
        'YC INSULATION': 'YC INSULATION',
        '佛山盈灿绝缘材料': 'Cách Điện Phô San Dinh Tỏa',
        '首页': 'Trang Chủ',
        '关于我们': 'Giới Thiệu',
        '产品中心': 'Sản Phẩm',
        '工厂展示': 'Nhà Máy',
        '联系我们': 'Liên Hệ',
        '专业绝缘套管制造商': 'Nhà Sản Xuất Ống Cách Điện Chuyên Nghiệp',
        '专注绝缘材料': 'Chuyên Vật Liệu Cách Điện',
        '年行业经验': 'Năm Kinh Nghiệm',
        '出口国家': 'Quốc Gia Xuất Khẩu',
        '合作客户': 'Khách Hàng Hợp Tác',
        '浏览产品': 'Xem Sản Phẩm',
        '联系我们': 'Liên Hệ',
        '硅树脂玻璃纤维套管': 'Ống Sợi Thủy Tinh Silicon',
        '内纤外胶玻璃纤维套管': 'Ống Sợi Thủy Tinh LớpTrong LớpNgoài',
        '内胶外纤玻璃纤维套管': 'Ống Sợi Thủy Tinh LớpTrong LớpNgoài',
        'PVC涂层玻璃纤维管': 'Ống Sợi Thủy Tinh PVC',
        '硅胶管': 'Ống Silicon',
        'PVC套管': 'Ống PVC',
        '波纹管': 'Ống Gợn Sóng',
        'PET伸缩编织网管': 'Lưới Đan PET Co Giãn',
        '热缩管': 'Ống Co Nhiệt',
        '品质保障': 'Đảm Bảo Chất Lượng',
        '自主生产': 'Sản Xuất Tự Chủ',
        '快速发货': 'Giao Hàng Nhanh',
        '全球出口': 'Xuất Khẩu Toàn Cầu',
        '专业服务': 'Dịch Vụ Chuyên Nghiệp',
        '定制服务': 'Dịch Vụ Tùy Chỉnh',
        '合作伙伴': 'Đối Tác',
        '地址': 'Địa Chỉ',
        '电话': 'Điện Thoại',
        '邮箱': 'Email',
        '在线询价': 'Yêu Cầu Báo Giá',
        '您的姓名': 'Tên Của Bạn',
        '公司名称': 'Tên Công Ty',
        '感兴趣的产品': 'Sản Phẩm Quan Tâm',
        '留言': 'Tin Nhắn',
        '提交': 'Gửi',
        '快速链接': 'Liên Kết Nhanh',
        '主要产品': 'Sản Phẩm Chính',
        '联系方式': 'Thông Tin Liên Hệ',
        '版权所有': 'Bản Quyền',
        '玻璃纤维套管': 'Ống Cách Điện',
        '厂家': 'Nhà Sản Xuất',
        '绝缘套管供应商': 'Nhà Cung Cấp Ống Cách Điện',
        '耐温范围': 'Phạm Vi Nhiệt Độ',
        '耐压等级': 'Cấp Độ Chịu Áp',
        '认证标准': 'Tiêu Chuẩn Chứng Nhận',
        '最小起订量': 'Số Lượng Đặt Hàng Tối Thiểu',
        '交货期': 'Thời Gian Giao Hàng',
        '免费样品': 'Mẫu Miễn Phí',
        '查看详情': 'Xem Chi Tiết',
        '黄腊管': 'Ống Sáp Vàng',
        'PVC涂覆玻纤管': 'Ống Sợi Thủy Tinh Phủ PVC',
    },
    'th': {  # 泰语
        'YC INSULATION': 'YC INSULATION',
        '佛山盈灿绝缘材料': 'วัสดุฉนวนฝอซานหยิ่งชาน',
        '首页': 'หน้าแรก',
        '关于我们': 'เกี่ยวกับเรา',
        '产品中心': 'สินค้า',
        '工厂展示': 'โรงงาน',
        '联系我们': 'ติดต่อ',
        '专业绝缘套管制造商': 'ผู้ผลิตปลอกฉนวนกันความร้อนมืออาชีพ',
        '专注绝缘材料': 'เชี่ยวชาญวัสดุฉนวน',
        '年行业经验': 'ปีประสบการณ์',
        '出口国家': 'ประเทศส่งออก',
        '合作客户': 'ลูกค้าคู่ค้า',
        '浏览产品': 'ดูสินค้า',
        '联系我们': 'ติดต่อเรา',
        '硅树脂玻璃纤维套管': 'ปลอกเส้นใยแก้วซิลิโคน',
        '内纤外胶玻璃纤维套管': 'ปลอกเส้นใยแก้วชั้นในชั้นนอก',
        '内胶外纤玻璃纤维套管': 'ปลอกเส้นใยแก้วชั้นในชั้นนอก',
        'PVC涂层玻璃纤维管': 'ท่อเส้นใยแก้วเคลือบ PVC',
        '硅胶管': 'ท่อซิลิโคน',
        'PVC套管': 'ท่อ PVC',
        '波纹管': 'ท่อลอน',
        'PET伸缩编织网管': 'ปลอกถัก PET ยืดหด',
        '热缩管': 'ท่อหดตัว',
        '品质保障': 'รับประกันคุณภาพ',
        '自主生产': 'ผลิตเอง',
        '快速发货': 'จัดส่งเร็ว',
        '全球出口': 'ส่งออกทั่วโลก',
        '专业服务': 'บริการมืออาชีพ',
        '定制服务': 'บริการตามสั่ง',
        '合作伙伴': 'พันธมิตร',
        '地址': 'ที่อยู่',
        '电话': 'โทรศัพท์',
        '邮箱': 'อีเมล',
        '在线询价': 'สอบถามราคา',
        '您的姓名': 'ชื่อของคุณ',
        '公司名称': 'ชื่อบริษัท',
        '感兴趣的产品': 'สินค้าที่สนใจ',
        '留言': 'ข้อความ',
        '提交': 'ส่ง',
        '快速链接': 'ลิงก์ด่วน',
        '主要产品': 'สินค้าหลัก',
        '联系方式': 'ข้อมูลติดต่อ',
        '版权所有': 'สงวนลิขสิทธิ์',
        '玻璃纤维套管': 'ปลอกฉนวน',
        '厂家': 'ผู้ผลิต',
        '绝缘套管供应商': 'ผู้จำหน่ายปลอกฉนวน',
        '耐温范围': 'ช่วงอุณหภูมิ',
        '耐压等级': 'ระดับทนแรงดัน',
        '认证标准': 'มาตรฐานรับรอง',
        '最小起订量': 'ปริมาณสั่งซื้อขั้นต่ำ',
        '交货期': 'ระยะเวลาจัดส่ง',
        '免费样品': 'ตัวอย่างฟรี',
        '查看详情': 'ดูรายละเอียด',
        '黄腊管': 'ท่อขี้ผึ้งเหลือง',
        'PVC涂覆玻纤管': 'ท่อเส้นใยแก้วเคลือบ PVC',
    },
    'id': {  # 印尼语
        'YC INSULATION': 'YC INSULATION',
        '佛山盈灿绝缘材料': 'Material Isolasi Foshan Yingcan',
        '首页': 'Beranda',
        '关于我们': 'Tentang Kami',
        '产品中心': 'Produk',
        '工厂展示': 'Pabrik',
        '联系我们': 'Hubungi',
        '专业绝缘套管制造商': 'Produsen Selubung Isolasi Profesional',
        '专注绝缘材料': 'Spesialis Material Isolasi',
        '年行业经验': 'Tahun Pengalaman',
        '出口国家': 'Negara Ekspor',
        '合作客户': 'Pelanggan Mitra',
        '浏览产品': 'Lihat Produk',
        '联系我们': 'Hubungi Kami',
        '硅树脂玻璃纤维套管': 'Selubung Fiberglass Silikon',
        '内纤外胶玻璃纤维套管': 'Selubung Fiberglass Lapisan',
        '内胶外纤玻璃纤维套管': 'Selubung Fiberglass Lapisan',
        'PVC涂层玻璃纤维管': 'Tabung Fiberglass Lapisan PVC',
        '硅胶管': 'Tabung Silikon',
        'PVC套管': 'Tabung PVC',
        '波纹管': 'Tabung Bergelombang',
        'PET伸缩编织网管': 'Selubung Rajut PET',
        '热缩管': 'Tabung Susut Panas',
        '品质保障': 'Jaminan Kualitas',
        '自主生产': 'Produksi Mandiri',
        '快速发货': 'Pengiriman Cepat',
        '全球出口': 'Ekspor Global',
        '专业服务': 'Layanan Profesional',
        '定制服务': 'Layanan Kustom',
        '合作伙伴': 'Mitra',
        '地址': 'Alamat',
        '电话': 'Telepon',
        '邮箱': 'Email',
        '在线询价': 'Permintaan Penawaran',
        '您的姓名': 'Nama Anda',
        '公司名称': 'Nama Perusahaan',
        '感兴趣的产品': 'Produk yang Diminati',
        '留言': 'Pesan',
        '提交': 'Kirim',
        '快速链接': 'Tautan Cepat',
        '主要产品': 'Produk Utama',
        '联系方式': 'Informasi Kontak',
        '版权所有': 'Hak Cipta',
        '玻璃纤维套管': 'Selubung Isolasi',
        '厂家': 'Produsen',
        '绝缘套管供应商': 'Pemasok Selubung Isolasi',
        '耐温范围': 'Rentang Suhu',
        '耐压等级': 'Tingkat Tahan Tegangan',
        '认证标准': 'Standar Sertifikasi',
        '最小起订量': 'Jumlah Pesanan Minimum',
        '交货期': 'Waktu Pengiriman',
        '免费样品': 'Sampel Gratis',
        '查看详情': 'Lihat Detail',
        '黄腊管': 'Tabung Lilin Kuning',
        'PVC涂覆玻纤管': 'Tabung Fiberglass Lapisan PVC',
    },
    'tr': {  # 土耳其语
        'YC INSULATION': 'YC INSULATION',
        '佛山盈灿绝缘材料': 'Foshan Yingcan Yalıtım Malzemeleri',
        '首页': 'Ana Sayfa',
        '关于我们': 'Hakkımızda',
        '产品中心': 'Ürünler',
        '工厂展示': 'Fabrika',
        '联系我们': 'İletişim',
        '专业绝缘套管制造商': 'Profesyonel Yalıtım Manşon Üreticisi',
        '专注绝缘材料': 'Yalıtım Malzemesi Uzmanı',
        '年行业经验': 'Yıllık Deneyim',
        '出口国家': 'İhracat Ülkesi',
        '合作客户': 'İş Ortağı',
        '浏览产品': 'Ürünleri Gör',
        '联系我们': 'Bize Ulaşın',
        '硅树脂玻璃纤维套管': 'Silikon Fiberglas Manşon',
        '内纤外胶玻璃纤维套管': 'İç Fiber Dış Yapışkan Manşon',
        '内胶外纤玻璃纤维套管': 'İç Yapışkan Dış Fiber Manşon',
        'PVC涂层玻璃纤维管': 'PVC Kaplı Fiberglas Tüp',
        '硅胶管': 'Silikon Tüp',
        'PVC套管': 'PVC Tüp',
        '波纹管': 'Oluklu Tüp',
        'PET伸缩编织网管': 'PET Örgü Manşon',
        '热缩管': 'Isı Daraltma Tüpü',
        '品质保障': 'Kalite Güvencesi',
        '自主生产': 'Kendi Üretimi',
        '快速发货': 'Hızlı Teslimat',
        '全球出口': 'Küresel İhracat',
        '专业服务': 'Profesyonel Hizmet',
        '定制服务': 'Özel Hizmet',
        '合作伙伴': 'Ortaklar',
        '地址': 'Adres',
        '电话': 'Telefon',
        '邮箱': 'E-posta',
        '在线询价': 'Fiyat Sor',
        '您的姓名': 'Adınız',
        '公司名称': 'Şirket Adı',
        '感兴趣的产品': 'İlgilenilen Ürünler',
        '留言': 'Mesaj',
        '提交': 'Gönder',
        '快速链接': 'Hızlı Bağlantılar',
        '主要产品': 'Ana Ürünler',
        '联系方式': 'İletişim Bilgileri',
        '版权所有': 'Tüm Hakları Saklıdır',
        '玻璃纤维套管': 'Yalıtım Manşon',
        '厂家': 'Üretici',
        '绝缘套管供应商': 'Yalıtım Manşon Tedarikçisi',
        '耐温范围': 'Sıcaklık Aralığı',
        '耐压等级': 'Voltaj Seviyesi',
        '认证标准': 'Sertifikasyon Standartları',
        '最小起订量': 'Minimum Sipariş Miktarı',
        '交货期': 'Teslimat Süresi',
        '免费样品': 'Ücretsiz Numune',
        '查看详情': 'Detayları Gör',
        '黄腊管': 'Sarı Mum Tüpü',
        'PVC涂覆玻纤管': 'PVC Kaplı Fiberglas Tüp',
    },
    'ar': {  # 阿拉伯语
        'YC INSULATION': 'YC INSULATION',
        '佛山盈灿绝缘材料': 'م materials عزل فوشان ينغكان',
        '首页': 'الرئيسية',
        '关于我们': 'عنا',
        '产品中心': 'المنتجات',
        '工厂展示': 'المصنع',
        '联系我们': 'اتصل بنا',
        '专业绝缘套管制造商': 'مصنع أكمام عزل محترف',
        '专注绝缘材料': 'متخصص في مواد العزل',
        '年行业经验': 'سنوات خبرة',
        '出口国家': 'دول التصدير',
        '合作客户': 'عملاء شركاء',
        '浏览产品': 'تصفح المنتجات',
        '联系我们': 'تواصل معنا',
        '硅树脂玻璃纤维套管': 'كم ألياف زجاج سيليكون',
        '内纤外胶玻璃纤维套管': 'كم ألياف زجاج طبقي',
        '内胶外纤玻璃纤维套管': 'كم ألياف زجاج طبقي',
        'PVC涂层玻璃纤维管': 'أنبوب ألياف زجاج مغلف PVC',
        '硅胶管': 'أنبوب سيليكون',
        'PVC套管': 'أنبوب PVC',
        '波纹管': 'أنبوب مموج',
        'PET伸缩编织网管': 'كم شبكة PET',
        '热缩管': 'أنبوب انكماش حراري',
        '品质保障': 'ضمان الجودة',
        '自主生产': 'إنتاج ذاتي',
        '快速发货': 'توصيل سريع',
        '全球出口': 'تصدير عالمي',
        '专业服务': 'خدمة محترفة',
        '定制服务': 'خدمة مخصصة',
        '合作伙伴': 'الشركاء',
        '地址': 'العنوان',
        '电话': 'الهاتف',
        '邮箱': 'البريد الإلكتروني',
        '在线询价': 'طلب عرض سعر',
        '您的姓名': 'اسمك',
        '公司名称': 'اسم الشركة',
        '感兴趣的产品': 'المنتجات المهمة',
        '留言': 'الرسالة',
        '提交': 'إرسال',
        '快速链接': 'روابط سريعة',
        '主要产品': 'المنتجات الرئيسية',
        '联系方式': 'معلومات الاتصال',
        '版权所有': 'جميع الحقوق محفوظة',
        '玻璃纤维套管': 'كم عزل',
        '厂家': 'المصنع',
        '绝缘套管供应商': 'مورد أكمام العزل',
        '耐温范围': 'نطاق درجة الحرارة',
        '耐压等级': 'مستوى الجهد',
        '认证标准': 'معايير الشهادة',
        '最小起订量': 'الحد الأدنى للطلب',
        '交货期': 'فترة التسليم',
        '免费样品': 'عينة مجانية',
        '查看详情': 'عرض التفاصيل',
        '黄腊管': 'أنبوب شمع أصفر',
        'PVC涂覆玻纤管': 'أنبوب ألياف زجاج مغلف PVC',
    }
}

# SEO翻译
SEO_TRANSLATIONS = {
    'vi': {
        '玻璃纤维套管厂家哪家好？UL认证绝缘套管供应商18年 | YC INSULATION': 
            'Nhà Sản Xuất Ống Cách Điện Tốt Nhất? UL认证 Nhà Cung Cấp Ống Cách Điện 18 Năm | YC INSULATION',
        '玻璃纤维套管厂家,绝缘套管供应商,硅树脂玻纤管,UL认证套管,VDE认证,耐高温套管,佛山盈灿,YC INSULATION':
            'nhà sản xuất ống cách điện,nhà cung cấp ống cách điện,ống sợi thủy tinh silicon,UL certifié,ống chịu nhiệt,Foshan YC,YC INSULATION',
    },
    'th': {
        '玻璃纤维套管厂家哪家好？UL认证绝缘套管供应商18年 | YC INSULATION':
            'ผู้ผลิตปลอกฉนวนที่ดีที่สุด? ULผู้จำหน่ายปลอกฉนวน 18 ปี | YC INSULATION',
        '玻璃纤维套管厂家,绝缘套管供应商,硅树脂玻纤管,UL认证套管,VDE认证,耐高温套管,佛山盈灿,YC INSULATION':
            'ผู้ผลิตปลอกฉนวน,ผู้จำหน่ายปลอกฉนวน,ปลอกเส้นใยแก้วซิลิโคน,UL certified,ปลอกทนความร้อน,Foshan YC,YC INSULATION',
    },
    'id': {
        '玻璃纤维套管厂家哪家好？UL认证绝缘套管供应商18年 | YC INSULATION':
            'Produsen Selubung Isolasi Terbaik? UL Certified Pemasok Selubung Isolasi 18 Tahun | YC INSULATION',
        '玻璃纤维套管厂家,绝缘套管供应商,硅树脂玻纤管,UL认证套管,VDE认证,耐高温套管,佛山盈灿,YC INSULATION':
            'produsen selubung isolasi,pemasok selubung isolasi,selubung fiberglass silikon,UL certified,selubung tahan panas,Foshan YC,YC INSULATION',
    },
    'tr': {
        '玻璃纤维套管厂家哪家好？UL认证绝缘套管供应商18年 | YC INSULATION':
            'En İyi Yalıtım Manşon Üreticisi? UL Certified Yalıtım Manşon Tedarikçisi 18 Yıl | YC INSULATION',
        '玻璃纤维套管厂家,绝缘套管供应商,硅树脂玻纤管,UL认证套管,VDE认证,耐高温套管,佛山盈灿,YC INSULATION':
            'yalıtım manşon üreticisi,yalıtım manşon tedarikçisi,silikon fiberglas manşon,UL certified,yüksek sıcaklık manşonu,Foshan YC,YC INSULATION',
    },
    'ar': {
        '玻璃纤维套管厂家哪家好？UL认证绝缘套管供应商18年 | YC INSULATION':
            'أفضل مصنع أكمام عزل؟ UL معتمد مورد أكمام العزل 18 سنة | YC INSULATION',
        '玻璃纤维套管厂家,绝缘套管供应商,硅树脂玻纤管,UL认证套管,VDE认证,耐高温套管,佛山盈灿,YC INSULATION':
            'مصنع أكمام عزل,مورد أكمام عزل,كم ألياف زجاج سيليكون,UL معتمد,كم مقاوم للحرارة,Foshan YC,YC INSULATION',
    }
}

def translate_html(content, lang):
    """翻译HTML内容"""
    translated = content
    
    # 应用基本翻译
    trans_dict = TRANSLATIONS.get(lang, {})
    for zh, foreign in trans_dict.items():
        translated = translated.replace(zh, foreign)
    
    # 应用SEO翻译
    seo_dict = SEO_TRANSLATIONS.get(lang, {})
    for zh, foreign in seo_dict.items():
        translated = translated.replace(zh, foreign)
    
    # 更新hreflang属性
    # 阿拉伯语需要RTL支持
    if lang == 'ar':
        translated = translated.replace('<html lang="zh-CN">', '<html lang="ar" dir="rtl">')
        translated = translated.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
    else:
        translated = translated.replace('<html lang="zh-CN">', f'<html lang="{lang}">')
        translated = translated.replace('<htmllang="en">', f'<html lang="{lang}">')
    
    return translated

def translate_homepage(lang):
    """翻译主页"""
    # 读取中文主页
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻译内容
    translated = translate_html(content, lang)
    
    # 更新语言切换链接
    translated = update_lang_switch(translated, lang)
    
    # 写入新文件
    output_file = f'index-{lang}.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f'✅ 已生成: {output_file}')
    return output_file

def update_lang_switch(content, lang):
    """更新语言切换器"""
    # 将当前语言标记为active
    lang_map = {
        'vi': ('Tiếng Việt', 'index-vi.html'),
        'th': ('ไทย', 'index-th.html'),
        'id': ('Indonesia', 'index-id.html'),
        'tr': ('Türkçe', 'index-tr.html'),
        'ar': ('العربية', 'index-ar.html'),
    }
    
    if lang in lang_map:
        lang_name, lang_file = lang_map[lang]
        # 找到语言切换区域并更新
        content = re.sub(
            r'<a href="index\.html" class="active">中文</a>',
            '<a href="index.html">中文</a>',
            content
        )
        content = re.sub(
            f'<a href="{lang_file}">',
            f'<a href="{lang_file}" class="active">',
            content
        )
    
    return content

def main():
    """主函数"""
    print("开始批量翻译主页...")
    print("=" * 50)
    
    # 翻译主页
    for lang in ['vi', 'th', 'id', 'tr', 'ar']:
        output = translate_homepage(lang)
        print(f"   {output} 已完成")
    
    print("=" * 50)
    print("主页翻译完成！")

if __name__ == '__main__':
    main()