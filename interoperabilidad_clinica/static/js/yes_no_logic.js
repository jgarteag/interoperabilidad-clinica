window.onload = function() {
    var oposDonation = document.getElementById('opossition_donation');
    var oposDonationDate = document.getElementById('opossition_donation_date');
    var antiWillDoc = document.getElementById('antiquated_will_document');
    var antiWillDocDate = document.getElementById('antiquated_will_document_date');

    oposDonation.onchange = function() {
        var selectedText = this.options[this.selectedIndex].text;
        oposDonationDate.disabled = (selectedText == 'Si') ? false : true;
    }

    antiWillDoc.onchange = function() {
        var selectedText = this.options[this.selectedIndex].text;
        antiWillDocDate.disabled = (selectedText == 'Si') ? false : true;
    }
}