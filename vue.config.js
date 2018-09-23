module.exports = {
  devServer: {
    disableHostCheck: true,
  },

  baseUrl: process.env.NODE_ENV === 'production'
    ? '/unbgames-platform/'
    : '/'
}
