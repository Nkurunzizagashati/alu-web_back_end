export default function updateUniqueItems(arg) {
  if (!(arg instanceof Map)) throw new Error('Cannot process');
  for (const item of arg.keys()) {
    if (arg.get(item) === 1) {
      arg.set(item, 100);
    }
  }
}
