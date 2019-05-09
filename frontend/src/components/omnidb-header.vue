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
              <b-button>Overview</b-button>
              <b-button>Downloads</b-button>
              <b-dropdown right text="Documentation">
                <b-dropdown-item>Item 1</b-dropdown-item>
                <b-dropdown-item>Item 2</b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item>Item 3</b-dropdown-item>
              </b-dropdown>
              <b-button>Community</b-button>
              <b-button>Sponsors</b-button>

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
  inject:['EventBus']
}

</script>
