/**
 * YC INSULATION GEO 自动跳转
 * 根据访问者IP地理位置自动跳转到对应语言版本
 * 
 * 修改：关闭自动跳转，改为显示语言选择提示
 */

(function() {
    const GEO_REDIRECT_VERSION = '2.0.0';
    const STORAGE_KEY = 'yc_geo_redirected_v2';
    
    // 语言名称映射
    const LANGUAGE_NAMES = {
        'zh': '中文',
        'en': 'English',
        'ko': '한국어',
        'vi': 'Tiếng Việt',
        'th': 'ไทย',
        'id': 'Bahasa Indonesia',
        'tr': 'Türkçe',
        'ar': 'العربية'
    };
    
    // 获取当前页面语言
    function getCurrentLanguage() {
        const path = window.location.pathname;
        const map = {
            'index-en.html': 'en',
            'index-ko.html': 'ko',
            'index-vi.html': 'vi',
            'index-th.html': 'th',
            'index-id.html': 'id',
            'index-tr.html': 'tr',
            'index-ar.html': 'ar'
        };
        for (let [file, lang] of Object.entries(map)) {
            if (path.includes(file)) return lang;
        }
        return 'zh'; // 默认中文
    }
    
    // 检测浏览器语言
    function detectBrowserLanguage() {
        const browserLang = navigator.language || navigator.userLanguage || 'zh-CN';
        const langCode = browserLang.split('-')[0].toLowerCase();
        
        const langMap = {
            'zh': 'zh',
            'en': 'en',
            'ko': 'ko',
            'vi': 'vi',
            'th': 'th',
            'id': 'id',
            'tr': 'tr',
            'ar': 'ar'
        };
        
        return langMap[langCode] || 'zh'; // 默认中文
    }
    
    // 显示语言选择提示（可选）
    function showLanguageHint(targetLang) {
        const currentLang = getCurrentLanguage();
        
        // 如果已经在正确语言页面，不显示提示
        if (currentLang === targetLang) return;
        
        // 中文用户直接不提示
        if (targetLang === 'zh') return;
        
        // 只显示一次提示
        if (sessionStorage.getItem(STORAGE_KEY)) return;
        sessionStorage.setItem(STORAGE_KEY, 'true');
        
        // 创建语言提示条
        const hint = document.createElement('div');
        hint.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: linear-gradient(135deg, #e25831 0%, #f6c954 100%);
            color: white;
            padding: 12px 20px;
            text-align: center;
            font-size: 14px;
            z-index: 10000;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
        `;
        
        const targetName = LANGUAGE_NAMES[targetLang] || targetLang;
        const targetFile = targetLang === 'zh' ? 'index.html' : `index-${targetLang}.html`;
        
        hint.innerHTML = `
            <span>🌍 This page is also available in ${targetName}</span>
            <a href="${targetFile}" style="
                background: white;
                color: #e25831;
                padding: 5px 15px;
                border-radius: 20px;
                text-decoration: none;
                font-weight: 600;
            ">Switch to ${targetName}</a>
            <button onclick="this.parentElement.remove()" style="
                background: none;
                border: none;
                color: white;
                cursor: pointer;
                font-size: 18px;
            ">×</button>
        `;
        
        document.body.appendChild(hint);
        document.body.style.paddingTop = '50px';
    }
    
    // 主函数 - 关闭自动跳转，仅显示提示
    async function initGeoRedirect() {
        console.log('[GEO] v' + GEO_REDIRECT_VERSION + ' - Auto-redirect disabled');
        
        // 检测目标语言
        const targetLang = detectBrowserLanguage();
        console.log('[GEO] Detected language preference:', targetLang);
        
        // 只显示提示，不自动跳转
        if (document.readyState === 'complete') {
            showLanguageHint(targetLang);
        } else {
            window.addEventListener('load', () => showLanguageHint(targetLang));
        }
    }
    
    // 页面加载后执行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGeoRedirect);
    } else {
        initGeoRedirect();
    }
})();
