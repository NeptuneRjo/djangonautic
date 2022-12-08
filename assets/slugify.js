const titleField = document.querySelector('input[name=title]')
const slugField = document.querySelector('input[name=slug]')

const slugify = (val) => {
	return val
		.toString()
		.toLowerCase()
		.trim()
		.replace(/&/g, '-and-')
		.replace(/[\s\W-]+/g, '-')
}

titleField.addEventListener('keyup', (e) => {
	slugField.setAttribute('value', slugify(titleField.value))
})
