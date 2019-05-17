<template>
<li
  :id="'omnidb_documents-lister_li-' + index"
  class="omnidb_documents-lister_li"
>

      <omnidb-documents-lister-svg
        :index="index"
        :item-height="itemHeight"
      >
      </omnidb-documents-lister-svg>

      {{item.title}}
</li>
</template>

<script>
import omnidbDocumentsListerSvg from './omnidb_documents-lister-svg.vue'

export default {
  name: 'omnidb-documents-lister-item',

  props: ['listItem', 'index'],

  data() {
    return {

        item: this.listItem,
        itemHeight: 0

    }
  },

  components: {
      omnidbDocumentsListerSvg
  },

  methods: {

      getLiHeight() {
        console.log('autalizou');

        this.$nextTick(function () {
          // DOM is now updated
          this.itemHeight = $('#omnidb_documents-lister_li-' + this.index ).height();
        })

          //return $('#omnidb_documents-lister_li-' + this.index ).height();

      },

      updateHeight: async function () {

          await this.$nextTick()

          this.itemHeight = $('#omnidb_documents-lister_li-' + this.index ).height();

      }

  },

  watch: {

      item: 'getLiHeight'

  },

  mounted() {

      this.getLiHeight();

      console.log($('#omnidb_documents-lister_li-' + this.index ).height());

  },

  updated() {
      this.$nextTick(function () {
          this.updateHeight();
      });
  }

}
</script>
