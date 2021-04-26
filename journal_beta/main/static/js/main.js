function show_side_block(){
    let side_block = document.getElementsByClassName('side_block')[0];
    let info = document.getElementsByClassName('info')[0];
    let side_block_styles = getComputedStyle(side_block);
    if (side_block_styles.left !== '0px'){
        side_block.style.setProperty('left', '0px');
        side_block.style.setProperty('box-shadow', 'rgba(0,0,0,0.16) 0 0 2px');
        info.innerHTML =
            '<span class="material-icons-outlined">\n' +
            '    close\n' +
            '</span>'
    } else{
        side_block.style.setProperty('left', '-5000px');
        side_block.style.setProperty('box-shadow', 'none');
        info.innerHTML =
            '<span class="material-icons-outlined">\n' +
            '    info\n' +
            '</span>'
    }
}