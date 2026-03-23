/**
 * GitHub OAuth 代理服务器
 * 部署到 Vercel 后即可使用
 */

// 从环境变量读取配置
const CLIENT_ID = process.env.OAUTH_CLIENT_ID
const CLIENT_SECRET = process.env.OAUTH_CLIENT_SECRET
const REDIRECT_URL = process.env.REDIRECT_URL || 'https://hemanja.github.io/ycsleeve.github.io/admin/'

// CORS 头
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization'
}

// 处理 OAuth 授权请求
export default async function handler(req, res) {
  // 处理 OPTIONS 请求
  if (req.method === 'OPTIONS') {
    res.status(200).json({})
    return
  }

  const { url, method } = req

  // 授权入口
  if (url.startsWith('/auth') && method === 'GET') {
    const scope = 'repo'
    const authUrl = `https://github.com/login/oauth/authorize?client_id=${CLIENT_ID}&scope=${scope}&redirect_uri=${REDIRECT_URL}callback`
    res.redirect(authUrl)
    return
  }

  // 回调处理
  if (url.startsWith('/callback') && method === 'GET') {
    const { code } = req.query

    if (!code) {
      res.status(400).json({ error: 'Missing code parameter' })
      return
    }

    try {
      // 交换 access token
      const tokenResponse = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          client_id: CLIENT_ID,
          client_secret: CLIENT_SECRET,
          code: code,
          redirect_uri: REDIRECT_URL
        })
      })

      const tokenData = await tokenResponse.json()

      if (tokenData.error) {
        res.status(400).json({ error: tokenData.error })
        return
      }

      // 重定向回前端并传递 token
      const redirectUrl = `${REDIRECT_URL}?access_token=${tokenData.access_token}&token_type=${tokenData.token_type}`
      res.redirect(redirectUrl)
      return
    } catch (error) {
      res.status(500).json({ error: error.message })
      return
    }
  }

  // 默认响应
  res.status(404).json({ error: 'Not found' })
}
