# YC CMS OAuth 服务器

GitHub OAuth 认证代理，用于 Decap CMS 后台登录。

## 🚀 快速部署到 Vercel

### 方式1：一键部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/nickyout/oauth-github&env=OAUTH_CLIENT_ID,OAUTH_CLIENT_SECRET,REDIRECT_URL)

### 方式2：手动部署

#### 步骤1：创建 GitHub OAuth App

1. 访问 https://github.com/settings/developers
2. 点击 "OAuth Apps" → "New OAuth App"
3. 填写：
   - **Application name**: YC INSULATION CMS
   - **Homepage URL**: https://hemanja.github.io/ycsleeve.github.io/
   - **Authorization callback URL**: https://你的域名.vercel.app/callback
4. 创建后记录 **Client ID** 和 **Client Secret**

#### 步骤2：部署到 Vercel

```bash
# 安装 Vercel CLI
npm install -g vercel

# 登录 Vercel
vercel login

# 部署
cd oauth-server
vercel
```

#### 步骤3：设置环境变量

在 Vercel 控制台设置环境变量：

- `OAUTH_CLIENT_ID`: GitHub OAuth Client ID
- `OAUTH_CLIENT_SECRET`: GitHub OAuth Client Secret
- `REDIRECT_URL`: https://hemanja.github.io/ycsleeve.github.io/admin/

#### 步骤4：更新 CMS 配置

在 `admin/config.yml` 中更新 `base_url`：

```yaml
backend:
  name: github
  repo: hemanja/ycsleeve.github.io
  branch: master
  base_url: https://你的域名.vercel.app
```

## 📝 使用说明

部署完成后：

1. 访问 https://hemanja.github.io/ycsleeve.github.io/admin/
2. 点击 "Login with GitHub"
3. 授权后即可进入 CMS 后台

## ⚠️ 安全提示

- 不要在代码中暴露 `OAUTH_CLIENT_SECRET`
- 确保回调地址与 GitHub OAuth App 中配置的一致
- 定期检查 GitHub OAuth App 的访问权限

---

更新时间：2026-03-24
