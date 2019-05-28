<template>
  <div class="omnidb_documents-lister_container">
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
  </div>
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
  .omnidb_documents-lister_container {
      position: fixed;
      top: 112px;
      right: 1rem;
      bottom: 0;
      padding: 0 1rem 0 0.5rem;

      ul.omnidb_documents-lister_ul {
          margin-bottom: 0;
          padding: 0.25rem;

          display: flex;
          flex-wrap: wrap;
          flex-direction: column;

              li.omnidb_documents-lister_li {
                  list-style: unset;

                  flex: 1 1 100%;
                  display: flex;
                  align-items: stretch;
                  justify-content: stretch;
                  min-height: 40px;

                  &> a {
                      flex: 1 1 100%;
                      font-size: 1.2rem;
                      font-weight: 200;
                      color: #c88181;

                      span {
                          display: inline-block;
                      }

                  }

                  svg {
                      flex: 0 0 16px;
                  }

                  &:nth-of-type(2n) > a span {
                     display: inline-block;
                     transform: translateX(-1rem);
                  }

              }
      }
  }
</style>
