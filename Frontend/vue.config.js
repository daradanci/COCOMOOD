module.exports = process.env.NODE_ENV === 'development' ? {
  devServer: {
    proxy: {
      '/': {
        target: 'http://192.168.250.244:8080/', // Replace with your API URL
        changeOrigin: true,
        secure: false,
        pathRewrite: { '^/': '' }, // Remove /api from the endpoint
      },
    },
  },
} : {};
