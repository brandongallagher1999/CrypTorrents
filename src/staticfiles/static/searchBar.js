class SearchBar extends React.Component
{
    render()
    {
        return(

            <form className="form-inline">
                 <i className="fas fa-search" aria-hidden="true"></i>
                   <input className="form-control form-control-lg w-50 mx-auto" type="text" placeholder="Search"
                  aria-label="Search"> 
                    </input>
                    <a className="btn btn-danger" href="#" color="#DC143C">Search</a>
            </form>

        );
    }




}

ReactDOM.render(<SearchBar />, document.getElementById("r_searchbar"));