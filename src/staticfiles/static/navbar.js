class Navbar extends React.Component {

  render() {

    return (
      <h4>
      <nav className="navbar navbar-expand-lg bg-dark">
      <a className="navbar-brand" href="#"><h4>CrypTorrents</h4></a>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
              <a className="nav-item nav-link active" href="#">Login<span className="sr-only">(current)</span></a>
              <a className="nav-item nav-link disabled" href="#">TV Shows (Coming Soon)</a>
              <a className="nav-item nav-link active" href="#">Donate</a>
          </div>
      </div>
    </nav>
    </h4>
    );
  }
}

ReactDOM.render(< Navbar />, document.getElementById('r_navbar'));