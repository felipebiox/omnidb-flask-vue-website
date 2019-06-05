// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import $ from 'jquery'
import App from './App'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
require('./assets/scss/style.scss')

Vue.config.productionTip = false
Vue.use(BootstrapVue)

//MIXINS
import EventBusMixin from './components/mixins/EventBus'

//CUSTOM DIRECTIVES
import './components/directives/omnidb-scroll'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  router,
  components: { App },
  mixins: [
    EventBusMixin
  ],
  template: '<App/>'
})
