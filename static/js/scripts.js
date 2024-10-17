function showLoading(event) {
    event.preventDefault(); 

    const formData = new FormData(event.target);
    const url = formData.get('url');

    document.getElementById('loading').style.display = 'block';
    
    event.target.submit();
}

window.onload = function() {
    document.getElementById('loading').style.display = 'none';
};
