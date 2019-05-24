<template>

  <header>

    <div class="custom">

        <div id="gh-ribbon"><a href="https://github.com/OmniDB/OmniDB"><img src="../assets/img/headers/gh-adapted.png" alt="Fork me on GitHub"></a>
        </div>
    </div>

		<div class="border-top"></div>

		<div id="header1">
			<div class="container">
				<div class="row">
					<div class="span12">
						<nav class="">
							<div class="mod-languages">

                <ul class="lang-inline">
                  <li class="lang-active" dir="ltr">
                    <a href="/en/documentation-en/introduction-en">
                    <img src="/media/mod_languages/images/en_gb.gif" alt="English (UK)" title="English (UK)">						</a>
                  </li>
                </ul>

              </div>

						</nav>
					</div>
				</div>
			</div>
		</div>
		<div id="header2">
			<div class="container">
				<div class="row">

					<div id="logo" class="col-3">

            <div class="custom">
      	       <div>
                 <a id="brand-link" title="OmniDB Brand" href="/index.php"><img src="../assets/img/headers/omnidb.png" alt="OmniDB"></a>
               </div>
            </div>

					</div>

					<div class="col-9 d-flex">
            <b-button-group class="ml-auto">

              <b-button
                v-for="( page, pageIndex ) in pages"
                :key="pageIndex"
                @click="(page.url) ? emitLoadPage( { 'pageUrl': page.url, 'pageIndex': pageIndex, 'childIndex': null } ) : preventDefault()"
                variant="transparent"
              >

                  <template v-if="page.label == 'Documentation'">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32" height="32" viewBox="0 0 32 32">

                          <path
                            d="M 6 1 L 26 1 L 26 29 L 6 29 Z"
                            fill="none" stroke="#819ec8" stroke-width="1"/>

                          <path
                            d="M 27 3 L 30 4 L 30 32 L 8 32 L 7 30"
                            fill="none" stroke="#819ec8" stroke-width="1"/>

                          <path
                            d="M 12 8 24 8"
                            fill="none" stroke="#819ec8" stroke-width="1"/>

                          <path
                            d="M 12 12 24 12"
                            fill="none" stroke="#819ec8" stroke-width="1"/>

                          <path
                            d="M 12 16 24 16"
                            fill="none" stroke="#819ec8" stroke-width="1"/>

                        </svg>
                  </template>

                  {{ page.label }}

                  <template v-if="page.children && page.children.length > 0">

                      <b-dropdown>
                        <b-dropdown-item
                          v-for="( child, childIndex ) in page.children"
                          :key="childIndex"
                          @click="(child.url) ? emitLoadPage( { 'pageUrl': child.url, 'pageIndex': pageIndex, 'childIndex': childIndex } ) : preventDefault()"
                        >
                            {{ child.label }}
                        </b-dropdown-item>
                      </b-dropdown>

                  </template>

              </b-button>

            </b-button-group>
					</div>
				</div>
			</div>
		</div>
	</header>

</template>


<script>

export default {
  name: 'omnidb-header',
  inject: ['EventBus'],
  props: {
    pages: {
      type: Array,
      required: true,
      default: [
        {
          url: '/',
          label: 'Overview',
          status: true
        }
      ]
    }
  },
  data () {
    return {

    }
  },
  methods: {
    emitLoadPage(pageConfig) {
      this.EventBus.$emit( 'omnidb:load-page', { 'pageUrl': pageConfig.pageUrl, 'pageIndex': pageConfig.pageIndex, 'childIndex': pageConfig.childIndex } );
    },
    preventDefault() {
      this.preventDefault;
    }
  }
}

</script>
