# YC INSULATION CMS 后台管理系统

## 🎯 CMS方案

使用 **Netlify CMS (Decap CMS)** + **Netlify Identity**

**优势**：
- ✅ 免费托管
- ✅ 自带身份认证（无需OAuth配置）
- ✅ 自动部署
- ✅ 支持自定义域名
- ✅ 可视化产品管理

---

## 🚀 快速开始

### 步骤1：注册Netlify账号

1. 访问 https://app.netlify.com/signup
2. 使用GitHub账号注册

### 步骤2：导入网站

1. 在Netlify点击 "Add new site" → "Import an existing project"
2. 选择 "GitHub"
3. 授权并选择仓库 `hemanja/ycsleeve.github.io`
4. 构建设置：
   - Build command: 留空（静态网站无需构建）
   - Publish directory: `.`
5. 点击 "Deploy site"

### 步骤3：启用Identity服务

1. 进入网站设置：Site settings → Identity
2. 点击 "Enable Identity"
3. 配置注册方式：
   - Registration: "Invite only"（仅邀请注册）
   - External providers: GitHub（可选）

### 步骤4：启用Git Gateway

1. 在 Identity 设置中
2. 找到 Services → Git Gateway
3. 点击 "Enable Git Gateway"

### 步骤5：添加管理员

1. 回到 Identity 页面
2. 点击 "Invite users"
3. 输入你的邮箱地址
4. 收到邮件后点击链接设置密码

### 步骤6：访问CMS后台

访问：`https://你的站点名.netlify.app/admin/`

使用邮箱和密码登录即可！

---

## 📋 产品管理

### 添加新产品

1. 登录后台
2. 选择产品系列：
   - 玻璃纤维套管
   - 热缩管系列
   - 其他产品
3. 点击"新建产品"
4. 填写产品信息：
   - 产品名称（中英文）
   - 产品类型
   - 主图 + 产品图片
   - 技术参数
   - 应用领域
5. 点击"发布"

### 编辑产品

1. 在产品列表中找到要编辑的产品
2. 点击进入编辑界面
3. 修改内容
4. 点击"保存"或"发布"

### 上传图片

1. 在编辑界面点击图片区域
2. 选择"上传"或拖拽图片
3. 图片自动保存到 `images/products/`

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
└── others/                          # 其他产品
```

### 图片存储

```
images/
├── products/         # CMS上传的产品图片
├── scenes/           # 应用场景图
└── *.jpg/png         # 其他图片
```

---

## 🔧 自定义域名（可选）

1. 在Netlify进入 Domain settings
2. 点击 "Add custom domain"
3. 输入你的域名（如 ycinsulation.com）
4. 按照提示配置DNS

---

## 📚 相关文档

- [Decap CMS 文档](https://decapcms.org/docs/)
- [Netlify Identity 文档](https://docs.netlify.com/identity/identity/)
- [Netlify CMS 教程](https://www.netlifycms.org/docs/add-to-your-site/)

---

## ⚠️ 注意事项

1. **首次登录**需要先在Netlify添加管理员用户
2. **图片大小**建议压缩到600px宽度
3. **发布流程**：编辑 → 预览 → 保存草稿 → 发布
4. **自动备份**：每次发布会创建Git提交

---

## 🆘 常见问题

**Q: 无法登录后台？**
A: 确保已在Netlify Identity中添加用户并设置密码

**Q: 图片上传失败？**
A: 检查图片大小，建议先压缩

**Q: 发布后看不到更新？**
A: Netlify自动部署需要几秒，刷新页面即可

**Q: 想添加其他管理员？**
A: 在Netlify Identity页面邀请新用户

---

更新时间：2026-03-24
