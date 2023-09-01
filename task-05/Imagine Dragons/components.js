class Header extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <nav class="navbar">
      <div class="logo">
          <img src="./assets/navbar/logo.png" alt="Logo">
      </div>
      <div class="icons">
          <a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q" target="_blank" class="icon-link"><img src="/assets/navbar/spotify.png" alt="Spotify"></a>
          <a href="https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA" target="_blank" class="icon-link"><img src="/assets/navbar/youtube.svg" alt="YouTube"></a>
          <a href="https://twitter.com/Imaginedragons" target="_blank" class="icon-link"><img src="/assets/navbar/twitter.svg" alt="Twitter"></a>
          <a href="https://www.instagram.com/imaginedragons/" target="_blank" class="icon-link"><img src="/assets/navbar/instagram.svg" alt="Instagram"></a>
      </div>
  </nav>
          `
    }
  }
  customElements.define('main-header', Header);