<template>
  <div id="documentation" class="pt-4">
    <div class="container">

      <div class="row">

            <div class="col-12 col-lg-9">

                  <template

                    v-for="(ct_section, index) in documents">

                        <template
                        v-if="sectionStatus == index + 1">
                                <div
                                  class="card hA_cardFlow"
                                >

                                    <div class="card-header">
                                        <h1 class="text-left">
                                            {{ct_section.title}}
                                        </h1>
                                    </div>

                                    <div class="card-body">
                                        <section class="border-top my-4">

                                                <div v-html="ct_section.introtext">


                                                </div>

                                        </section>
                                    </div>

                                </div>
                        </template>

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
      documents: [],
      sectionStatus: 1
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

            this.documents = response.data.data;

            this.setStatus();

        })
        .catch(error => {
          console.log(error)
        })
    },

    setStatus(index) {
        let i = 0;
        for (i = 0; i < this.documents.length; i++) {
            this.documents[ i ].status = false;
        }
    },

    changeDocument(documentConfig) {

        //console.log( documentConfig.index, this.documents[ documentConfig.index ].status );

        let i = 0;

        for ( i=0; i < this.documents.length; i++) {

            this.documents[i].status = false;

        }

        this.documents[ documentConfig.index ].status = true;
        this.sectionStatus = documentConfig.index + 1;

    }

  },
  mounted () {
    this.getDocuments();

    let vueThis = this;

    this.EventBus.$on('omnidb:change-document', function(documentConfig) {

      vueThis.changeDocument(documentConfig);

    });

  }
}

</script>
