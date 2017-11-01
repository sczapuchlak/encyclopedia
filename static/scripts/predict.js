var oracle;
window.addEventListener('DOMContentLoaded', function () {
    oracle = new Oracle();
});
/**
 *  This class is used to predict the user input
 */
var Oracle = (function () {
    function Oracle(searches) {
        if (searches === void 0) { searches = []; }
        var _this = this;
        this.searches = searches;
        this.searchBox = null;
        this.suggestionList = null;
        //Get our search box from the dom
        this.searchBox = document.getElementById('term');
        //register the change event there
        this.searchBox.addEventListener('input', function () { return _this.filterSuggestions(); });
        this.searchBox.addEventListener('focus', function () { return _this.filterSuggestions(); });
        this.searchBox.addEventListener('blur', function (event) { return _this.searchBoxBlured(event); });
        //get the suggestion list from the dom
        this.suggestionList = document.getElementById('predictive');
        //get the searchs on the next tick (this allows the application to continue processing
        // w/o blocking for this event to finish)
        setTimeout(function () { return _this.getSearches(); }, 0);
    }
    /**
     * Request the searches from the server (the server will take care of the current user)
     */
    Oracle.prototype.getSearches = function () {
        var _this = this;
        console.log('getSearches');
        //open an http request
        //A more modern way to do this would be through the fetch
        //api, however I found this to be significantly slower in its current 
        //implementation
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'searches');
        //register what to do on any change to the ready state
        xhr.addEventListener('readystatechange', function (event) { return _this.requestStateChange(event.currentTarget); });
        //send the request
        xhr.send();
    };
    /**
     * Event handler for our XHR's ready state change event
     * @param {XMLHttpRequest} request - The xhr we used to requet data from the server
     */
    Oracle.prototype.requestStateChange = function (request) {
        console.log('requestStateChange');
        //if our request is done (XHRs are dumb about events, they fire 4 times and we only care about
        //the last one)
        if (request.readyState === request.DONE) {
            console.log('requestStateChange', 'DONE');
            //We wrap our JSON.parse in a try because it will
            //throw an error on invalid JSON, or array will remain
            //emptt in that case
            try {
                this.searches = JSON.parse(request.responseText).searches;
                console.log('requestStateChange', 'JSON Parsed', this.searches);
            }
            catch (e) {
                //I don't really care what happens on error, just want to know about it while testing
                console.error('error getting search data', e);
            }
        }
    };
    /**
     * Filter our suggestions based on what the user has entered in the textbox
     * this will use the searchBox.value to do the compare and is case insensitive
     */
    Oracle.prototype.filterSuggestions = function () {
        var _this = this;
        //look through our searches and filter out any that don't match
        //JS Array.prototype.filter takes an argument that is a function, this
        //function needs to return a boolean true will include the item, false
        //will not, I am looking for the index of our search term
        //and if it doesn't exist(-1) not including it
        var newSuggestions = this.searches.filter(function (s) { return s.toLowerCase().indexOf(_this.searchBox.value.toLowerCase()) > -1; });
        this.updateSuggestions(newSuggestions);
    };
    /**
     * Update the list of suggestions displayed to the user
     * @param {Array<string>}newSuggestions An array of the terms that match the current search term
     */
    Oracle.prototype.updateSuggestions = function (newSuggestions) {
        var _this = this;
        if (newSuggestions === void 0) { newSuggestions = []; }
        this.clearSuggestions();
        if (newSuggestions.length < 1) {
            this.suggestionList.setAttribute('class', 'hidden');
            return;
        }
        this.suggestionList.setAttribute('class', '');
        for (var i = 0; i < newSuggestions.length; i++) {
            this.suggestionList.appendChild(this.generateTermEntry(newSuggestions[i], i));
        }
        newSuggestions.forEach(function (term, index) { return _this.generateTermEntry(term, index); });
    };
    /**
     * Clear the children of our list of suggestions
     */
    Oracle.prototype.clearSuggestions = function () {
        //starting from the bottom, remove all children
        //from the list element
        while (this.suggestionList.hasChildNodes()) {
            this.suggestionList.removeChild(this.suggestionList.lastChild);
        }
    };
    /**
     * quickly generate a span with the right properties for our search list
     * @param {string} term - the text that will appear in the element
     * @param index - The index it is in, this is used to set the tab index
     */
    Oracle.prototype.generateTermEntry = function (term, index) {
        var _this = this;
        //create the span element
        var entryContainer = document.createElement('span');
        //set the tab index (that makes it focusable)
        entryContainer.setAttribute('tabindex', (index + 1).toString());
        //set the class
        entryContainer.setAttribute('class', 'search-suggestion');
        //add the text to the span
        entryContainer.appendChild(document.createTextNode(term));
        //register the click event (this will also fire on enter pressed while selected)
        entryContainer.addEventListener('click', function (event) { return _this.selectSuggestion(event.currentTarget); });
        //return the elemnt
        return entryContainer;
    };
    /**
     * The event handler for the span click event, this sets the
     * value of the search box to the innerHTML of the span selected
     * @param selected - The span that was selected
     */
    Oracle.prototype.selectSuggestion = function (selected) {
        console.log('selectSuggestion', selected);
        this.searchBox.value = selected.innerHTML;
        this.updateSuggestions();
    };
    /**
     * The event handler for a blur event on the searchBox. We need to make sure that the
     * blur event doesn't clear the suggestions if the user is clicking one of the suggestions
     * this will try and control that
     * @param event Click event that triggered this function
     */
    Oracle.prototype.searchBoxBlured = function (event) {
        if (event.relatedTarget) {
            var newFocus = event.relatedTarget;
            var newFocusClass = newFocus.getAttribute('class');
            if (newFocusClass.indexOf('search-suggestion') > -1) {
                return;
            }
        }
        this.updateSuggestions();
    };
    return Oracle;
}());
