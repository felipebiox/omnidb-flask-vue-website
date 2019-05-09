<template>

  <div id="app">

    <omnidb-header></omnidb-header>
    <div id="page-content">
      <div class="container">
        <h1>Testes</h1>
        <img src="./assets/logo.png">
        <router-view/>
      </div>
    </div>

  </div>

</template>

<script>
import OmnidbHeader from './components/omnidb-header.vue';

export default {
  name: 'App',
  components: {
    OmnidbHeader
  },
  inject:['EventBus']
}
</script>

<style lang="sass">

  @import './assets/scss/style.scss'

</style>
