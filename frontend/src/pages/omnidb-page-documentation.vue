<template>
  <div id="documentation" class="pt-4">
    <div class="container">

      <div class="row">

            <div class="col-12 col-lg-9">

                  <template v-for="ct_section in documents">
                      <section class="border-top my-4">

                              <h1 class="text-left">
                                {{ct_section.title}}
                              </h1>

                              <div v-html="ct_section.introtext">


                              </div>

                      </section>

                  </template>

            </div>

            <div class="col-lg-3">

                  <template v-if="documents.length > 0">

                      <omnidb-documents-lister
                        :documents="documents"
                      >
                      </omnidb-documents-lister>

                  </template>

            </div>

        </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import omnidbDocumentsLister from './../components/omnidb_documents-lister/omnidb_documents-lister.vue'

export default {
  data () {
    return {
      documents: []
    }
  },
  components: {
    omnidbDocumentsLister
  },
  inject:['EventBus'],
  methods: {

    getDocuments () {

      const path = 'http://localhost:5000/api/getDocumentation';
      const config = {
        method: 'GET',
        mode: 'no-cors',
        headers: {
          'Access-Control-Allow-Origin': 'http://localhost:8080',
          'Access-Control-Allow-Headers': 'Authorization',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
          'Access-Control-Allow-Credentials': true,
          //'Content-Type': 'application/json',
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        //credentials: 'same-origin',
        credentials: true
      }

      axios.get( path, config )
        .then(response => {
          this.documents = response.data.data
        })
        .catch(error => {
          console.log(error)
        })
    }

  },
  mounted () {
    this.getDocuments();
  }
}

</script>
