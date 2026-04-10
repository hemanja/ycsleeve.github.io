# 网站多语言翻译方案

## 翻译方法

### 方法一：使用在线翻译工具（推荐）
1. 复制中文页面内容
2. 使用专业翻译工具翻译：
   - 越南语：Google Translate / DeepL
   - 泰语：Google Translate（泰语支持好）
   - 印尼语：Google Translate
   - 土耳其语：Google Translate / DeepL
   - 阿拉伯语：DeepL（中东语言支持好）

### 方法二：使用专业翻译API
```bash
# 使用 Python googletrans 库
pip install googletrans==4.0.0-rc1
```

### 方法三：使用AI辅助翻译
- ChatGPT / Claude 批量翻译
- 保持技术参数不变，只翻译描述性文字

## 注意事项

1. **保持HTML结构**：不要修改标签、类名、ID
2. **技术参数不变**：如耐温范围、电压等级等数字和单位
3. **链接路径不变**：产品链接、图片路径保持原样
4. **SEO优化**：标题、描述需要自然，符合搜索习惯
5. **RTL语言**：阿拉伯语需要添加 `dir="rtl"` 属性

## 批量生成命令

```bash
# 生成各语言版本主页
python3 translate-homepage.py

# 生成各语言版本产品页
python3 translate-products.py
```

## 当前进度

### 主页
- [x] index.html (中文)
- [x] index-en.html (英语)
- [x] index-ko.html (韩语)
- [ ] index-vi.html (越南语) - 需要重新翻译
- [ ] index-th.html (泰语) - 需要重新翻译
- [ ] index-id.html (印尼语) - 需要重新翻译
- [ ] index-tr.html (土耳其语) - 需要重新翻译
- [ ] index-ar.html (阿拉伯语) - 需要重新翻译

### 产品页面
- [ ] fiberglass-wax.html 系列 (7个语言)
- [ ] pvc-hose.html 系列 (7个语言)
- [ ] pet-braided-sleeve.html 系列 (7个语言)
- [ ] fiberglass-inner-fiber.html 系列 (7个语言)
- [ ] fiberglass-inner-rubber.html 系列 (7个语言)