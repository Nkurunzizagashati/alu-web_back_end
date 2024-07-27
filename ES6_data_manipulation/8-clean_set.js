export default function cleanSet(set, str) {
  if (
    !set
    || !str
    || typeof set !== 'object'
    || typeof str !== 'string'
  ) {
    return '';
  }

  return [...set]
    .filter(
      (el) => typeof el === 'string' && el.startsWith(str),
    )
    .map((el) => el.replace(str, ''))
    .join('-');
}
