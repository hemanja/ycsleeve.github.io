# YC INSULATION CMS 后台管理系统

## 🚀 快速开始

### 1. 访问后台

网站部署后，访问：`https://hemanja.github.io/ycsleeve.github.io/admin/`

### 2. 登录方式

使用GitHub账号登录（需要OAuth配置）

---

## 📋 OAuth配置步骤

### 步骤1：创建GitHub OAuth App

1. 访问 https://github.com/settings/developers
2. 点击 "OAuth Apps" → "New OAuth App"
3. 填写信息：
   - **Application name**: YC INSULATION CMS
   - **Homepage URL**: https://hemanja.github.io/ycsleeve.github.io/
   - **Authorization callback URL**: https://yc-cms-oauth.vercel.app/callback
4. 创建后记录 **Client ID** 和 **Client Secret**

### 步骤2：部署OAuth代理到Vercel

**方式A：一键部署**

点击按钮部署到Vercel：

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/nickyout/oauth-github)

**方式B：手动部署**

1. Fork仓库：https://github.com/nickyout/oauth-github
2. 在Vercel导入该仓库
3. 设置环境变量：
   - `OAUTH_CLIENT_ID`: 你的GitHub Client ID
   - `OAUTH_CLIENT_SECRET`: 你的GitHub Client Secret
   - `REDIRECT_URL`: https://hemanja.github.io/ycsleeve.github.io/admin/

### 步骤3：更新配置

在 `admin/config.yml` 中更新 `base_url` 为你的Vercel域名。

---

## 📦 产品管理

### 添加新产品

1. 登录后台
2. 选择产品系列（玻璃纤维套管/热缩管/其他）
3. 点击"新建产品"
4. 填写产品信息：
   - 产品名称
   - 英文名称
   - 产品类型
   - 主图和产品图片
   - 技术参数
   - 应用领域
5. 点击"发布"

### 编辑产品

1. 在产品列表中找到要编辑的产品
2. 点击进入编辑界面
3. 修改内容后点击"保存"

### 上传图片

1. 在编辑界面点击"选择图片"
2. 选择本地图片文件
3. 图片会自动上传到 `images/products/` 目录

---

## 🎨 内容结构

### 产品页面结构

```
products/
├── fiberglass-inner-fiber.html      # 4KV内纤外胶
├── fiberglass-silicone-resin.html   # 1500V硅树脂
├── fiberglass-inner-rubber.html     # 内胶外纤
├── fiberglass-wax.html              # 黄腊管
├── dingwen-tube.html                # 定纹管
├── high-temp-seal-tube.html         # 耐高温密封管
├── fiberglass-ecigarette.html       # 电子烟专用管
├── heatshrink/                      # 热缩管系列
│   ├── single-wall.html
│   └── dual-wall.html
└── others/                          # 其他产品
    ├── corrugated-tube.html
    └── silicone-tube.html
```

### 图片存储

```
images/
├── products/                        # CMS上传的产品图片
├── scenes/                          # 应用场景图
└── *.jpg/png                        # 其他图片
```

---

## 🔧 本地开发

### 运行本地CMS

```bash
# 安装依赖
npm install -g decap-server

# 运行本地服务器
npx decap-server

# 访问 http://localhost:3000/admin/
```

---

## 📚 相关文档

- [Decap CMS 文档](https://decapcms.org/docs/)
- [GitHub OAuth 配置](https://decapcms.org/docs/github-backend/)
- [Vercel 部署指南](https://vercel.com/docs)

---

## ⚠️ 注意事项

1. **首次使用**需要完成OAuth配置才能登录
2. **图片大小**建议压缩到600px宽度以内
3. **发布流程**：编辑 → 预览 → 保存草稿 → 发布
4. **备份**：每次发布会自动创建Git提交

---

## 🆘 常见问题

**Q: 无法登录后台？**
A: 检查OAuth配置是否正确，Client ID和Secret是否匹配

**Q: 图片上传失败？**
A: 检查图片大小是否过大，建议先压缩

**Q: 发布后看不到更新？**
A: GitHub Pages需要几分钟更新，等待后刷新

---

更新时间：2026-03-24
