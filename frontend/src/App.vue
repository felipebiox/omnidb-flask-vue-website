<template>

  <div id="app">

    <omnidb-header :pages="pages"></omnidb-header>



    <div id="page-content">

        <template v-for="page in pages">

          <template v-if="page.status">

            <template v-if="page.templateName == 'overview'">
              <omnidb-page-overview></omnidb-page-overview>
            </template>

            <template v-if="page.templateName == 'documentation'">
              <omnidb-page-documentation></omnidb-page-documentation>
            </template>

          </template>

        </template>

    </div>

    <div class="container">
      <h1>Testes</h1>
      <img src="./assets/logo.png">
      <router-view/>
    </div>

  </div>

</template>

<script>
import OmnidbHeader from './components/omnidb-header.vue';

//Pages
import OmnidbPageOverview from './pages/omnidb-page-overview.vue';
import OmnidbPageDocumentation from './pages/omnidb-page-documentation.vue';

export default {
  name: 'App',
  components: {
    OmnidbHeader,
    OmnidbPageOverview,
    OmnidbPageDocumentation
  },
  inject:['EventBus'],
  data () {
    return {
      pages: [
        {
          url: '/',
          label: 'Overview',
          status: true,
          templateName: 'overview'
        },
        {
          url:  '/documentation',
          label: 'Documentation',
          status: false,
          templateName: 'documentation'
        }
      ]
    }
  },

  methods: {

    getIndexPageTemplateByStatus() {
      let arr = this.pages;

      for (var i=0, iLen=arr.length; i<iLen; i++) {

        if (arr[i].status == true) return i;
      }

    },

    getIndexPageTemplateByUrl(value) {
      let arr = this.pages;

      for (var i=0, iLen=arr.length; i<iLen; i++) {

        if (arr[i].url == value) return i;
      }

    },

    changePageContent(value) {

      let oldIndex = this.getIndexPageTemplateByStatus(),
          newIndex = this.getIndexPageTemplateByUrl(value);

      this.pages[oldIndex].status = false;
      this.pages[newIndex].status = true;



      console.log(oldIndex, this.pages[newIndex].status);

    }

  },

  mounted() {
    let vueThis = this;

    this.EventBus.$on('omnidb:load-page', function(value) {
      //console.log(value)

      vueThis.changePageContent(value);

    });
  }
}
</script>

<style lang="sass">

  @import './assets/scss/style.scss'

</style>
