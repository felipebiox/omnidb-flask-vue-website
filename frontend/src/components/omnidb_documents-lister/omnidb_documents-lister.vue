<template>
    <ul
      class="omnidb_documents-lister_ul"
    >
      <template v-for="(ct_section, sectionIndex) in documents">

          <omnidb-documents-lister-item
            v-if="loadChild"

            :list-item="ct_section"
            :index="sectionIndex"
          >
          </omnidb-documents-lister-item>

      </template>
    </ul>
</template>

<script>
import omnidbDocumentsListerItem from './omnidb_documents-lister-item.vue'

export default {

  name: 'omnidb-documents-lister',

  props: {

      documents: {
          type: Array,
          required: true,
          default: []
      }

  },

  data() {
    return {

        loadChild: false

    }
  },

  components: {
    omnidbDocumentsListerItem
  },

  methods: {

  },

  mounted() {

      this.loadChild = true;

  }

}

</script>

<style lang="scss">

  ul.omnidb_documents-lister_ul {
      padding: 0.25rem;

      display: flex;
      flex-wrap: wrap;
      flex-direction: column;

          li.omnidb_documents-lister_li {
              list-style: unset;

              flex: 1 1 100%;
              display: flex;

              svg {
                  flex: 0 0 16px;
              }

          }
  }

</style>
