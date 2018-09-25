import '@babel/polyfill'
import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import VueParticles from 'vue-particles'
Vue.use(VueParticles)


Vue.config.productionTip = false


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
