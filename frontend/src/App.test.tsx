import { renderToStaticMarkup } from 'react-dom/server'
import { describe, expect, it } from 'vitest'
import { App } from './App'

describe('tela inicial', () => {
  it('identifica o projeto como em desenvolvimento sem anunciar recursos inexistentes', () => {
    const markup = renderToStaticMarkup(<App />)

    expect(markup).toContain('<h1 id="title">Caô!</h1>')
    expect(markup).toContain('Contas, salas e partidas chegam nos próximos incrementos.')
  })
})
