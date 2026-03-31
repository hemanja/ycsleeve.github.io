# YC INSULATION GEO 优化方案

## 当前状态（2026-03-31）

### ✅ 已完成
- 基础 SEO 元标签
- Organization Schema（公司信息）
- WebSite Schema（网站搜索）
- 多语言支持（8种语言）
- 响应式设计
- 产品技术参数表

### ❌ 缺失（GEO 关键）
- ❌ 问答式标题和内容
- ❌ 详细的 Product Schema
- ❌ FAQPage 结构化数据
- ❌ BreadcrumbList 导航
- ❌ 快速答案区块
- ❌ 跨平台内容链接（LinkedIn、YouTube）
- ❌ 客户评价/案例展示
- ❌ 数据对比表、步骤清单

---

## 优化计划

### 第一步：答案优先型内容优化

#### 1.1 产品页面标题改造
**现有**：`内纤外胶玻纤管 4KV-10KV - YC INSULATION`
**优化**：`4KV玻璃纤维套管耐温多少？内纤外胶结构有什么优势？| YC INSULATION`

#### 1.2 快速答案区块
在产品页面顶部添加：
```
快速答案：
✅ 耐温范围：-60°C ~ +200°C
✅ 耐压等级：4KV / 7KV / 10KV
✅ 击穿电压：≥10000V（4KV型）
✅ 认证标准：UL / VDE / SGS
✅ 最小起订量：1000米
✅ 交货期：7-15天
```

#### 1.3 问答式内容结构
- "什么是内纤外胶玻纤管？"
- "4KV和10KV有什么区别？"
- "如何选择合适的耐压等级？"
- "内纤外胶和外纤内胶哪个更好？"

---

### 第二步：AI-readable 标记

#### 2.1 完善 Product Schema
```json
{
  "@type": "Product",
  "name": "4KV内纤外胶玻纤管",
  "description": "内层玻璃纤维编织，外层硅橡胶涂层，耐温-60°C~+200°C，耐压4KV，击穿电压≥10000V",
  "brand": {
    "@type": "Brand",
    "name": "YC INSULATION"
  },
  "manufacturer": {
    "@type": "Organization",
    "name": "佛山盈灿绝缘材料"
  },
  "material": "玻璃纤维 + 硅橡胶",
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "name": "耐压等级",
      "value": "4KV"
    },
    {
      "@type": "PropertyValue",
      "name": "耐温范围",
      "value": "-60°C ~ +200°C"
    },
    {
      "@type": "PropertyValue",
      "name": "击穿电压",
      "value": "≥10000V"
    },
    {
      "@type": "PropertyValue",
      "name": "认证标准",
      "value": "UL, VDE, SGS"
    }
  ],
  "offers": {
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "询价",
    "availability": "https://schema.org/InStock",
    "minimumOrderQuantity": "1000米",
    "deliveryLeadTime": "7-15天"
  }
}
```

#### 2.2 FAQPage 结构化数据
```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "4KV内纤外胶玻纤管的耐温范围是多少？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "4KV内纤外胶玻纤管的连续使用温度范围为-60°C ~ +200°C，短期可承受更高温度。"
      }
    },
    {
      "@type": "Question",
      "name": "最小起订量是多少？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "最小起订量为1000米，可根据客户需求提供定制长度。"
      }
    },
    {
      "@type": "Question",
      "name": "交货期需要多久？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "常规规格7-15天交货，定制规格需根据具体情况确认。"
      }
    },
    {
      "@type": "Question",
      "name": "产品有哪些认证？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "我们的产品通过UL、VDE、SGS等国际认证，符合RoHS环保标准。"
      }
    }
  ]
}
```

#### 2.3 BreadcrumbList
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "首页",
      "item": "https://ycsleeve.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "玻璃纤维套管系列",
      "item": "https://ycsleeve.com/products/fiberglass-series.html"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "内纤外胶玻纤管 4KV-10KV",
      "item": "https://ycsleeve.com/products/fiberglass-inner-fiber.html"
    }
  ]
}
```

---

### 第三步：跨平台信任证据链

#### 3.1 LinkedIn 内容
- 创建公司主页
- 发布产品实测文章
- 分享客户案例

#### 3.2 YouTube 视频
- 产品演示视频（已有部分）
- 嵌入到产品页面
- 添加视频结构化数据

#### 3.3 客户评价
- 添加客户评价区块
- 展示出口国家数据
- 展示认证证书

---

### 第四步：追踪 AI 引用率

#### 4.1 追踪方法
1. 每天用 Perplexity.ai 搜索：
   - "fiberglass sleeve manufacturer China"
   - "4KV fiberglass sleeve temperature rating"
   - "inner fiber outer rubber fiberglass tube"

2. 检查是否引用 YC INSULATION

3. 分析 Google Search Console：
   - "发现"流量报告
   - 搜索查询数据

4. 使用 SEO.ai 等工具追踪 AI 搜索能见度

---

## 实施优先级

### 高优先级（立即执行）
1. ✅ 完善 Product Schema
2. ✅ 添加 FAQPage
3. ✅ 添加快速答案区块
4. ✅ 改造产品页面标题为问答式

### 中优先级（本周内）
1. ⏳ 添加数据对比表
2. ⏳ 添加 BreadcrumbList
3. ⏳ 创建 LinkedIn 公司主页
4. ⏳ 添加客户评价区块

### 低优先级（本月内）
1. ⏳ 发布 LinkedIn 产品文章
2. ⏳ 录制 YouTube 产品演示
3. ⏳ 设置 AI 引用追踪系统

---

## 预期效果

### 短期（1-2周）
- Google Search Console 收录更新
- Perplexity.ai 可能开始引用

### 中期（1-3个月）
- Gemini/GPT 开始推荐
- "发现"流量增长 50%+

### 长期（3-6个月）
- 成为 AI 搜索"标准答案"
- 自然流量增长 200%+

---

更新时间：2026-03-31
执行人：OpenClaw Agent
