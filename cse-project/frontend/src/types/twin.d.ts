import 'twin.macro'
import styledComponent from 'styled-components'
import { css as cssProperty } from 'styled-components'

declare module 'twin.macro' {
  const styled: typeof styledComponent
  const css: typeof cssProperty
}