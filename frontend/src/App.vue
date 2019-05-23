<template>

  <div id="app">

    <omnidb-header :pages="pages"></omnidb-header>



    <div id="page-content">

        <template v-for="page in pages">

          <template v-if="page.status">

            <template v-if="page.templateName == 'overview'">

                <omnidb-page>

                    <omnidb-page-overview></omnidb-page-overview>

                </omnidb-page>

            </template>

            <template v-if="page.templateName == 'documentation'">

                <omnidb-page>

                    <omnidb-page-documentation></omnidb-page-documentation>

                </omnidb-page>

            </template>

          </template>

        </template>

    </div>

  </div>

</template>

<script>
import OmnidbHeader from './components/omnidb-header.vue';
import OmnidbPage from './components/omnidb-page.vue';

//Pages
import OmnidbPageOverview from './pages/omnidb-page-overview.vue';
import OmnidbPageDocumentation from './pages/omnidb-page-documentation.vue';

export default {
  name: 'App',
  components: {
    OmnidbHeader,
    OmnidbPage,
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
          templateName: 'documentation',
          children: [
            /*{
              url: '/documentation',
              label: '1- Introduction',
              status: false,
              templateName: 'documentation'
            }*/
          ]
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

    changePageContent(pageConfig) {

      let oldIndex = this.getIndexPageTemplateByStatus();
          //newIndex = this.getIndexPageTemplateByUrl(value);

      this.pages[oldIndex].status = false;

      this.pages[ pageConfig.pageIndex ].status = true;

      if (pageConfig.childIndex) {
        this.pages[ pageConfig.pageIndex ].children[ pageConfig.childIndex ].status = true;
      }

      //console.log(pageConfig.childIndex, this.pages[1].children[0]);

    }

  },

  mounted() {
    let vueThis = this;

    this.EventBus.$on('omnidb:load-page', function(pageConfig) {
      //console.log(value)

      vueThis.changePageContent(pageConfig);

    });
  }
}
</script>

<style lang="sass">

  @import './assets/scss/style.scss'

</style>
